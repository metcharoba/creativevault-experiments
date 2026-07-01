# AGENTS.md — 70_design_experiments

Design work in this folder follows the **Reference-first mimic** route.
Canonical sources (read these first):
- `reference_first_mimic_workflow_v0_2.md` — **the route (gated; current).**
- `reference_first_mimic_workflow_v0_1.md` — previous route, kept for history.
- `reference_first_mimic_validation_summary_v0_1.md` — rationale + §6 cautions.
- `_rfm_template/` — copy this whole folder to start a build; `00_GATES.md` is
  the per-build checklist. Auto screenshot helper: `tools/rfm_shot.py`.
- Wrapped as the invocable skill — Claude Code:
  `.claude/skills/reference-first-mimic/`, Codex: `~/.codex/skills/reference-first-mimic/`.
  Both wrap this AGENTS.md + `workflow_v0_2.md` (the source of truth) and refuse
  to run outside CreativeVault. Added 2026-06-17.

This file adds the bias-avoidance learned from reviewing all artifacts on 2026-06-13.
It applies to every agent (Codex included) doing design work here.

## Standard route (do every build) — HARD GATES
0. **GATE 0 🔒 — brief & scope (the USER confirms).** Before any design, confirm
   purpose/use + required content in `notes/brief.md`. Web/LP: hero message + primary
   CTA + rough scope (how many links / nav items / sections; desktop+mobile).
   Poster/flyer/single image: list EVERY required field and confirm each value one by
   one; unknowns = [PLACEHOLDER]. **Never invent / auto-fill / add an unrequested
   field.** No user "OK" → do not pick references / do not design.
1. Pick register/intent — and keep it DIFFERENT from recent builds (see "Known bias").
2. Present 3 strong non-SaaS / non-card references (name/URL/why/borrow/don't-borrow).
   **GATE 1 🔒 — the USER picks the lead.** Do not self-pick; wait for "これがいい".
   Record the pick in `notes/reference_candidates.md`.
2b. Screenshot the chosen lead (run from inside the build dir):
   `python3 ../tools/rfm_shot.py "<url>" screenshots/refs/lead_firstview.png`
   (auto-default; if SUSPECT/FAIL the user
   captures manually, same path). **GATE 2 🔒 — a real, looked-at screenshot must
   exist before any decompose/build.** No file → STOP.
3. Write the explicit **avoid-list** and **aim-list** up front (highest-leverage step).
4. Decide materials FIRST. **Use external material aggressively** for photo /
   print / artwork / archive registers — Dia-style museum editorial,
   publication, archive, photography-led pages collapse into a weak CSS-block
   approximation if you fall back to "self-made shapes". Allowed sources (record
   URL + license + attribution in `notes/materials_used`):
   - CC0 / Public Domain (Wikimedia Commons, museum open-access)
   - CC-BY / CC-BY-SA (record attribution string + link)
   - Official press kits / brand assets per their stated terms
   - Reference screenshots for observation only (fair use; not redistributed)
   - Self-made shapes (use for diagram / icon / type-led pieces, not by default)
   Fonts: OFL, self-hosted. Same for any runtime JS/CSS library (Three.js,
   etc.): vendor it under `assets/js/vendor/` (or similar) from the start,
   not a CDN `<script src>` / importmap. See "Recurring weaknesses" below.
5. Build ONE self-contained artifact (`index.html`, or `.png`/`.pdf` for print).
   **Web/LP only — GATE 3 is TWO-step 🔒**, both signed off by the USER before
   building the rest of the page:
   - **3a Hero look:** render the hero first-view ALONE
     (`screenshots/hero_checkpoint.png`); USER confirms direction/feeling.
   - **3b Structure:** write `notes/structure_proposal.md` enumerating EXACT
     nav labels (not "4 items"), section order with IDs, what lives in each
     section, mobile nav behavior, link count, and which fields stay
     `[PLACEHOLDER]`. USER ticks each one. **Hero "looks good" is NOT structure
     approval.** No sign-off → do NOT build the rest yet.
   Posters / single images skip GATE 3.
6. Render and actually look at screenshots (desktop first-view, full, mobile —
   or detail crops for print).
7. Write `notes/self_evaluation`: 0–5 scores, honest residual AI-ness, the
   difference vs recent builds, and one concrete next change.

Deliverable shape: artifact + `notes/{reference_observation, materials_used,
build_log, self_evaluation}.md` + screenshots. (This holds even for one-shot
poster/flyer builds made via a design skill — still write a self_evaluation and
record fonts/licenses.)

## Known bias to AVOID (reviewed 2026-06-13, all 9 artifacts)
The collection collapses into two poles plus a few house-tics. Do not reinforce
them — diversify on purpose.
- **Two poles**: quiet riso/archival editorial  ⇄  loud primary-color pop/comic.
  Under-explored, prefer these next: mono / one-color minimal typography;
  CC0 photo-led editorial; diagram / map / data-led; organic / tactile material;
  3D / print-material; Japanese vertical-set layout.
- **Overused motif**: "SIGNAL / transmission" (Signal Dept, Signal Cabinet,
  Creative Signal Night) and the copy "fragments / experiments / future / ideas".
  Reach for fresh vocabulary and metaphor.
- **House-tics**: halftone dots + print misregistration; cream/bone paper with a
  red + blue (+yellow) palette; condensed-bold (loud) or high-contrast serif+italic
  (quiet). Try at least one build that explicitly BANS these.

## Recurring weaknesses (from the self-evaluations + the 2026-06-13 review)
- **Per-element treatment goes uniform.** Placement gets broken well, but every
  same-kind element (cards, photo mounts, stickers, speech bubbles, info panels)
  defaults to one frame / shadow / cut / texture, which reads templated. Vary the
  treatment element by element.
- **Non-uniformity stacked too thick (added 2026-06-15).** 逆方向の失敗もある。
  描画モード(treatment)で既に十分非均一なら、サイズ・配置の追加軸を**乗せない**。
  「same-kind elements ≥3 patterns」は下限であって積み増せばよいわけではない。
  整列が register の核(diagram / scientific editorial / data-led)では、追加軸は
  逆に register を弱める。STEP D で主軸の非均一を 1 つ選び、追加軸は register と
  相反しないかを確認してから乗せる。bird_voice_time_chart_v0_1 の修正で実証。
- **Observation fidelity.** Builds tend to decompose references from memory rather
  than a real capture. **Now a hard gate (GATE 2):** observe at least ONE real
  reference screenshot before building. If a brief cites reference images and none
  are attached, obtain/observe one (or ask) before starting.
- **Concept-first decoration.** Start from visual language + references + avoid/aim,
  and let any (fictional) theme follow. Do NOT start from a pre-named concept and
  decorate it.
- **Procedural main visual に逃げない / route 事前相談（added 2026-06-16）.**
  image-led register（劇画 / photo-led editorial / archive / publication）では、
  **主役 visual を self-made polygons / 自前ペン線で組むのは silent register killer**。
  STEP D の avoid/aim 書く時点で「主役が procedural に寄りそう」と感じたら、決め打ち
  前に **route 候補（CC0 photo + heavy processing / 既存素材合成 / 自前）を 2-3 で
  並べて user に「これでいいか」を相談**。途中で「方向間違い」と自分で見えたら、
  v0.1 を user に見せる前に pivot 提案する（"ここまで来たので確認" は時間を user に
  押し付ける）。`maeda_kekkon_monogatari_v0_1` で実証：v0.1 = procedural 劇画顔（NG）、
  v0.2 以降 = CC0 王貞治 photo + threshold/halftone 処理（劇画 register 直撃）。
- **GPT生成への早期移行フロー（added 2026-06-16）.**
  似顔絵 / アメコミ / 劇画 / 商品ビジュアル / photo-to-illustration など、
  **主役画像の品質が成果物の 70% 以上を決める案件**では、Codex 内で無理に
  image_gen / CSS / PIL 生成を続けない。次のどれかに当てはまったら、user に
  明示して **GPT生成へ移行**する：
  - Codex の `image_gen` がチャット上には出るが、workspace に保存できる実ファイル
    パスを返さない / 見つけられない。
  - 1 回目の主役ビジュアルが「似ていない」「気持ち悪い」「register が違う」と
    判断できる。
  - text が重要で、Codex 側の生成/合成で破綻しそう（特に日本語題字）。
  - user が GPT / ChatGPT / 別生成ツールの方が良いと言った。

  移行時は以下を 1 セットで渡す：
  1. identity / product / subject の参照画像
  2. style reference（RFM の lead screenshot または強い参照 1-2 枚）
  3. exact readable text と禁止テキスト
  4. avoid list（余計な人物、日付、会場、ロゴ、watermark 等）
  5. 「生成できた PNG をこの build の `assets/` に戻す」保存先

  GPT から戻った画像は **素材として扱い直す**。`assets/` にコピーし、
  `materials_used.md` に「user-provided externally generated image」と記録し、
  Codex 側では必要最小限の整形（PNG/PDF化、2x化、余白調整、メモ更新）だけ行う。
  `maeda_kekkon_monogatari_v0_3` で実証：Codex 内生成は保存経路が破綻、GPT 生成の
  `MAEDA GETS MARRIED!` 版を取り込んだ方が品質・速度ともに良かった。
- **プロンプト設計先行のRFM分業（added 2026-06-18）.**
  `maeda_underwear_wedding_rfm_v0_1` で実証：主役絵・似顔絵・統合ポスターの品質が
  成果物を決める案件は、Codex が「作画」するのではなく、
  **RFMで参照を揉む → avoid/aimを明文化 → GPT生成プロンプトを作る → user/GPTで生成
  → CodexがQA・PNG/PDF化・記録**の分業が最も安定する。
  特に日本語題字を後貼りすると、読めても「絵の中の題字」ではなくラベル化して
  ズレやすい。題字まで作品性を決める場合は、最初から一括生成候補を出し、
  text が崩れたら Codex で雑に貼り直さず、再生成または route 再確認を行う。
  Codex の役割は、Gate管理・参照候補・スクショ観察・プロンプト設計・戻り画像の
  QA・納品整形に寄せる。
- **SVG/CSS/code-native 主役絵は許可制（added 2026-06-19）.**
  `maeda_wedding_fundoshi_edo_gag_rfm_v0_1` で失敗：浮世絵風の似顔・人物・主役絵を
  Codex SVG で作る判断は事前に弱さを予見できたのに、試作後の自己評価も甘かった。
  image-led で、似顔絵 / 人物 / 商品 / 劇画 / 浮世絵 / 主役イラスト / 物体感が成果物の
  70% 以上を決める場合、**SVG / CSS / canvas / PIL 等の code-native drawing を
  主役ビジュアル route として選ぶには、事前に user の明示許可が必要**。弱さが
  予見できる時は「A案」として勧めない。許可を取る時は
  「品質はラフスケッチ止まりになりやすい」「ダメなら GPT生成/外部素材に戻す」と
  リスクを先に言う。デフォルトは GPT画像生成・user提供画像・CC0/PD素材の加工・
  コラージュ等の route に寄せる。SVG は枠、題字、簡単な装飾、図解、マスク、配置の
  補助には使ってよいが、主役作画にしない。

  **例外: dot-based register は procedural が default route（added 2026-06-28）.**
  segment LCD（Game & Watch / Tiger LCD 系)、8-bit pixel art（Game Boy / Famicom 系)、
  sprite / chip 表示、ASCII art など、**register そのものが dot 単位で構成される**
  ケースでは、procedural（PIL / SVG / code-native）は register killer にならない —
  それが register の自然な medium。この場合は「許可制」ではなく、STEP D-E の
  route check で **最初から default 候補として強く提示**してよい。photo / 外部素材
  route は観察と register 抽出のみに使い、composite には使わない(冗長になる)。
  `retro_shooter_poster_rfm_v0_1` で実証: γ（CC-BY G&W 写真改造)を採用して 3 ver
  (v0.1〜v0.3)無駄にしてから pixel-only に pivot、最初から α(procedural)で行けば
  1 ver で着地できた。**route check の判定キー**: 「**主役の最小単位が dot か?**」
  yes ならこの例外、no なら上記許可制ルール。
- **External Asset First / Synthetic Fill (SF) route の運用知見（added 2026-06-22）.**
  `synthetic_fill_test_paper_collage_v0_1` で 4 variant を比較検証して出た反省。
  詳細フローは `reference_first_mimic_workflow_v0_2.md` §3 を正本とする。要点:
  - **mining + recomposite だけでは as-is に負ける**。design intent
    （「この hero で何を読ませたいか?」）を 1 行書き出して user 確認するまで
    PIL を開かない。intent を skip すると物理整合（lighting / shadow / edge）を
    捨てる分だけ as-is より悪い結果になる。今回 v3 で実証(user 指摘:
    「素材をただ置いただけ」)、v3.1 で intent A 確認後に復帰。
  - **「完成シーン生成 → そこから全 element 切り出し → 並べ直す」は構造的に弱い**。
    源側の coherence を捨てる分が design upside で取り戻せない。優先順位:
    (a) 外部素材から GPT で cutout / (b) 個別素材を GPT に単体生成 /
    (c) scene 生成からの mining は mutual context そのものが価値の時のみ。
  - **単一 hero 1 枚は GPT 一発生成も可**だが、複数 element が必要な register
    （ポスター / Web 構成 / multi-asset 合成）では一発生成だけでは弱い。
    Web 全体の素材不足分は「1 発 fill 生成 vs (a)/(b) の個別 route」を都度検討。
  - **BUILD-Gate sanity check を SF でも絶対 skip しない**。output PNG と
    lead screenshot を並べて自分で direction 判定してから user に見せる。
    今回 v3 で skip して "user に言われるまで気づかない" 状態を作った。
  - **brief は live document**。GATE 0 で決めた要素を後で変更した時
    (例:今回「hands なし」に切り替え)は PIL を開く前に brief を再 sync する。
- **CDNショートカットに逃げない / 依存はローカル vendor が default（added 2026-07-01）.**
  `creativevault_thought_gallery_rfm_v0_1` の hero を 3D 化した際、Three.js を
  jsdelivr CDN の importmap で読み込んだまま2回 push してしまい、自動セキュリティ
  レビュー（SRIなしのsupply-chain risk, MEDIUM）に指摘されてから
  `assets/js/vendor/three/` にローカル化する事後対応になった。このフォルダは
  フォントを OFL self-hosted にする慣習が既にあったのに、JS ライブラリには
  同じ発想を最初から適用できていなかった。**教訓**: 新しい外部ランタイム依存
  (JSライブラリ、CSSフレームワーク等)を足す時は、既存プロジェクトの vendoring
  慣習（フォント等）を見た時点で、CDN を仮置きせず最初からローカル vendor
  する。CDNは「後で直せばいい」対象ではなく、public に push する前に片付ける
  対象。
- **フォントは commit 前に 1-char render test（added 2026-06-16）.**
  STEP E でフォント候補が決まったら、`materials_used.md` に書く前に：
  ```python
  f = ImageFont.truetype(path, 100, index=idx)
  print(f.getbbox("テスト前田結婚物語！？"))   # 高さが妥当か
  ```
  subset / variable / ttc index 破損で text 消失するパターンが多い。**macOS bundled の
  Toppan Bunkyu (`/System/Library/PrivateFrameworks/.../Fonts/Subsets/`) は PIL から
  bbox 高さ 0** で render 不能（`maeda_kekkon_monogatari_v0_1` で実証、1 iteration ロス）。
  **OFL を `assets/` に curl 一本化が安全**（Noto Serif/Sans JP, Kaisei HarunoUmi,
  RocknRoll One, Yusei Magic 等）。Yusei Magic 等の display は `！？` 記号 glyph が
  薄いので、煽り文に含まれる記号も含めて test。fallback フォントも同様に。

## Before starting any new build
List the existing registers / motifs / palette / tics already in this folder, then
deliberately choose something different. New ≠ a fresh coat on the same two poles.

Fast-recall: `_inventory/builds.xlsx` (1 行 = 1 build。`register` / `palette` /
`pole_position` / `score` で過去作を横断 query 可能。STEP 0 で「pole_position が
"その他" の cold な register」を 5 秒で出すための台帳。新 build を作ったら 1 行
追加するか `_build_inventory.py` を更新して再生成)。Added 2026-06-17.
