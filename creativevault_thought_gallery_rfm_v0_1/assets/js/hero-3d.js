import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { MeshoptDecoder } from 'three/addons/libs/meshopt_decoder.module.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';

const MODEL_URL = 'assets/models/armillary-sphere-1771.glb';
const ASSEMBLE_MS = 2200;
const IDLE_SPEED = 0.12; // rad/sec

function easeOutBack(t) {
  const c1 = 1.4;
  const c3 = c1 + 1;
  return 1 + c3 * Math.pow(t - 1, 3) + c1 * Math.pow(t - 1, 2);
}

function randomUnitVector() {
  let x, y, z, lenSq;
  do {
    x = Math.random() * 2 - 1;
    y = Math.random() * 2 - 1;
    z = Math.random() * 2 - 1;
    lenSq = x * x + y * y + z * z;
  } while (lenSq === 0 || lenSq > 1);
  const len = Math.sqrt(lenSq);
  return { x: x / len, y: y / len, z: z / len };
}

function initHero3D(container, canvas) {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const scene = new THREE.Scene();

  const camera = new THREE.PerspectiveCamera(
    35,
    container.clientWidth / container.clientHeight,
    0.05,
    30
  );

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.05;
  if ('outputColorSpace' in renderer) renderer.outputColorSpace = THREE.SRGBColorSpace;

  const pmrem = new THREE.PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;

  const key = new THREE.DirectionalLight(0xfff3e0, 2.4);
  key.position.set(1.4, 2.2, 1.6);
  key.castShadow = true;
  key.shadow.mapSize.set(1024, 1024);
  key.shadow.camera.near = 0.1;
  key.shadow.camera.far = 6;
  key.shadow.camera.left = -0.6;
  key.shadow.camera.right = 0.6;
  key.shadow.camera.top = 0.6;
  key.shadow.camera.bottom = -0.6;
  key.shadow.bias = -0.0015;
  scene.add(key);
  scene.add(new THREE.AmbientLight(0xffffff, 0.4));

  const ground = new THREE.Mesh(
    new THREE.PlaneGeometry(8, 8),
    new THREE.ShadowMaterial({ opacity: 0.16 })
  );
  ground.rotation.x = -Math.PI / 2;
  ground.receiveShadow = true;
  scene.add(ground);

  const group = new THREE.Group();
  scene.add(group);

  // Visibility gating: pause the continuous idle-rotate loop when the hero
  // is scrolled out of view, so the tab isn't burning GPU/battery for a
  // decorative spin nobody is looking at.
  let isVisible = true;
  let idleActive = false;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        isVisible = entry.isIntersecting;
        if (isVisible) startIdleRotate();
      });
    },
    { threshold: 0.01 }
  );
  observer.observe(container);

  const loader = new GLTFLoader();
  loader.setMeshoptDecoder(MeshoptDecoder);
  loader.load(
    MODEL_URL,
    (gltf) => {
      const model = gltf.scene;

      const box = new THREE.Box3().setFromObject(model);
      const size = new THREE.Vector3();
      const center = new THREE.Vector3();
      box.getSize(size);
      box.getCenter(center);
      model.position.set(-center.x, -box.min.y, -center.z);

      const scatterRadius = Math.max(size.x, size.y, size.z);
      const meshes = [];

      model.traverse((obj) => {
        if (!obj.isMesh) return;
        obj.castShadow = true;
        obj.frustumCulled = false;

        const src = obj.geometry.getAttribute('position');
        const count = src.count;
        const original = new Float32Array(count * 3);
        const scatter = new Float32Array(count * 3);
        for (let i = 0; i < count; i++) {
          original[i * 3] = src.getX(i);
          original[i * 3 + 1] = src.getY(i);
          original[i * 3 + 2] = src.getZ(i);
          const dir = randomUnitVector();
          const mag = scatterRadius * (0.35 + Math.random() * 0.55);
          scatter[i * 3] = dir.x * mag;
          scatter[i * 3 + 1] = dir.y * mag;
          scatter[i * 3 + 2] = dir.z * mag;
        }
        const live = new THREE.BufferAttribute(original.slice(), 3);
        obj.geometry.setAttribute('position', live);
        meshes.push({ attr: live, original, scatter });
      });

      group.add(model);

      const diag = size.length();
      const dist = diag * 1.35;
      camera.position.set(dist * 0.55, size.y * 0.75, dist * 0.85);
      camera.lookAt(0, size.y * 0.4, 0);

      if (reduceMotion) {
        renderer.render(scene, camera);
      } else {
        runAssembly(meshes);
      }
    },
    undefined,
    (err) => {
      console.error('[hero-3d] failed to load model', err);
    }
  );

  function runAssembly(meshes) {
    const start = performance.now();
    group.rotation.y = -0.6;

    function tick(now) {
      const t = Math.min(1, (now - start) / ASSEMBLE_MS);
      const eased = easeOutBack(t);
      const chaos = 1 - THREE.MathUtils.clamp(eased, 0, 1);

      meshes.forEach(({ attr, original, scatter }) => {
        const arr = attr.array;
        for (let i = 0; i < arr.length; i++) {
          arr[i] = original[i] + scatter[i] * chaos;
        }
        attr.needsUpdate = true;
      });

      group.rotation.y = -0.6 + eased * 0.6;
      renderer.render(scene, camera);

      if (t < 1) {
        requestAnimationFrame(tick);
      } else {
        meshes.forEach(({ attr, original }) => {
          attr.array.set(original);
          attr.needsUpdate = true;
        });
        startIdleRotate();
      }
    }
    requestAnimationFrame(tick);
  }

  function startIdleRotate() {
    if (idleActive || reduceMotion || !isVisible) return;
    idleActive = true;
    let last = performance.now();
    function loop(now) {
      if (!isVisible) {
        idleActive = false;
        return;
      }
      const dt = (now - last) / 1000;
      last = now;
      group.rotation.y += IDLE_SPEED * dt;
      renderer.render(scene, camera);
      requestAnimationFrame(loop);
    }
    requestAnimationFrame(loop);
  }

  function resize() {
    const w = container.clientWidth;
    const h = container.clientHeight;
    if (w === 0 || h === 0) return;
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    renderer.setSize(w, h, false);
    renderer.render(scene, camera);
  }
  window.addEventListener('resize', resize);
  resize();
}

function boot() {
  const container = document.getElementById('hero');
  const canvas = document.getElementById('hero-canvas');
  if (!container || !canvas) return;
  if (!window.WebGLRenderingContext) return;
  try {
    initHero3D(container, canvas);
  } catch (err) {
    console.error('[hero-3d] init failed', err);
  }
}

boot();
