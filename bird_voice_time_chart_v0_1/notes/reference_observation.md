# Reference Observation (written FROM the screenshot — GATE 2)

- Lead: Florence Nightingale 「Diagram of the causes of mortality in the army in the East」(1858)
- Source URL: https://commons.wikimedia.org/wiki/File:Nightingale-mortality.jpg (Wikimedia Commons, Public Domain)
- Screenshot file: `screenshots/refs/lead_firstview.png` (captured: auto via `../tools/rfm_shot.py`)
- Capture note: rfm_shot.py OK — Wikimedia Commons の File ページに実画像が表示されている。**実際に目視した**。

## Decomposed from the screenshot
- **Composition:**
  - **2つの円形ローズダイアグラムが左右並列の small multiples**。中央軸で擬似ミラー。
  - 上にタイトル(古典セリフ・オールキャップス・複数行)、下に長文キャプション/凡例の縦列が続く。
  - 各円は中心点から放射する **12 のウェッジ**(月別)。
- **Whitespace / ma:**
  - 円の外側に大きな余白。円と円の谷間に小ラベル(月名・数値)を押し込む。中央寄せの「余白対称」感が支配的。
- **Material / texture:**
  - 紙の経年で温かいベージュ〜ペールイエロー。インクは退色した手刷り感(現代の鮮やかな印刷ではない)。
  - ハーフトーン点も見当ずれも**ない**(よくある riso 模倣の house-tic とは別物)。
- **Typography:**
  - 古典セリフのみ。サイズ階段(タイトル→デック→キャプション)で序列を作る。
  - すべて横組み・全角中央寄せ。スクリプト書体や条件付き太字は不使用。
- **Information density:**
  - 図そのものは静か(ウェッジ自体は太く単純)、しかし**ページの 1/3 は説明文**(脚注密度が高い)。
- **Non-uniformity:**
  - 12 のウェッジは「実データ」そのままなので、長さも面積もすべて違う。**規則的でない=テンプレ感が消える**最大の要因。
  - 左右の円の大きさ自体も非対称(=データ量の違いを画面で見せる)。
  - 色の重なり方も月ごとに違う(青のみの月もあれば 3 色全部出る月もある)。

## Borrow vs don't-borrow
- **Borrow:**
  - 放射状の時間軸(月 → 1日24時間 に置き換え)
  - 量を**ウェッジ面積/半径**で示すロジック
  - small multiples 構造(時間×種の二次元を「複数の小さい円」で分解)
  - 凡例を図の谷間/余白に直接書き込む編集感
  - 1〜2色 + 紙地の最小パレット
  - 図に対する「説明テキストの量」(キャプション/脚注を主役級に重く)
- **Don't-borrow:**
  - ヴィクトリア朝のオールキャップス装飾セリフ・銅版画タッチ
  - 紙の経年退色そのままの色(クリーム+赤+青はこの倉庫の house-tic に直結するので明示的に避ける)
  - 中央軸対称ミラー(これ自体が AI 模倣のレイアウト典型になりがち、片寄せに変える)

## Avoid-list (このビルドで明示的に禁ずる)
- ハーフトーン点描・印刷見当ずれ
- クリーム/ボーン紙 + 赤+青(+黄) パレット
- 中央寄せヒーロー、ピル型 CTA、frosted glass、ダークグラデ+浮きカード
- "SIGNAL / transmission / fragments / experiments / future / ideas" 語彙
- 太いコンデンスド見出し(loud pop 寄せ)
- 高コントラストのセリフ+斜体 quiet editorial(riso archive 寄せ)
- カードグリッドの均一配列

## Aim-list
- 放射状ダイアグラム(small multiples × 8 種)が版面の主役
- 文字は脇役。タイトルは**版面の左上または左下に寄せて非中央**
- 同種要素(8 つの species disc)を3パターン以上で**非均一**に描き分ける(下記参照)
- 色は **off-white の紙 + ダークインク 1 色 + アクセント 1 色** に限定。クリーム×赤青黄は禁
- フェイクデータでも「早朝にピーク・昼に谷」など、**読める偏り**を組み込む
- 視覚言語を上から下まで切れさせない(末尾のキャプションも図の一部に見える書式に)

## Per-element-treatment plan (recurring weakness 対策)
8 つの species disc を **同じテンプレで打ち抜かない**。少なくとも 3 パターンで治療を分ける:
- 4 つは **塗りウェッジ**(面積=回数)
- 2 つは **線のみのウェッジ**(枠線で活動時間帯を示す)
- 2 つは **点群**(ドットの密度で活動の量を示す)
- 加えて、ディスク自体のサイズも 2 段階で大小を作る(主要種は大きく)
- ラベル位置も統一しない:下にぶら下げる種・横に流す種・図の中央に置く種を混ぜる
- 一部のディスクは外周の時刻ティック数を間引く(全部 24 個ではなく、6/12/24 を混ぜる)
