# Self-Evaluation — bird_voice_time_chart_v0_1

Honest, not promotional. 0 = same as recent builds, 5 = clearly a different/strong output.

| Criterion | Score | Basis |
|-----------|------:|-------|
| Different picture than before | 4 | 倉庫の既存 9 作は (a) riso editorial / (b) loud pop の 2 極に偏っていた。本作は**ダイアグラム/計測**register で、図形主体・テラコッタ+森緑のパレット。明らかに違う画。 |
| Lead reference's composition actually used | 4 | Nightingale の (i) 放射状時間軸 (ii) 量=半径/面積 (iii) 1 主色 + 副色 + 紙地 (iv) 余白に直接書き込まれる凡例、を素直に持ってきた。「2 円 side-by-side」は意識的に「8 つ small multiples」へ展開した(模倣でなく構造の借用)。 |
| Generic-AI-LP feel reduced | 4 | 中央寄せヒーロー・グラデ・カードグリッドを避け、SVG で計算された具体的データ図を主役にした。AI生成画像なし。 |
| Material feel | 3 | リネン白の紙地 + ダークインクで「印刷物」感は出たが、本物の紙の繊維/版ずれは入れていない(意図的に避けた)。「データ印刷物」としては成立、本物の刷り物質感はもう一歩。 |
| Non-uniformity (same-kind elements not templated) | 4 | 6 つの描画モード + 3 段階サイズ + 3 パターン配置 + 2 種ラベル。8 つを「同じ型で打ち抜いた」感は避けられた。 |
| Screen-as-artwork feel | 3 | 「情報グラフィックの 1 枚絵」として読める。ただし装飾的な訴求力は控えめで、X タイムラインで一目を引くかは控えめな寄り。 |
| Strong top-to-bottom (not only the top) | 4 | METHOD パラグラフに accent 色の短罫、フッターに mono クレジット 2 行 + 罫。上で強く、下も崩れていない。 |
| Register differs from recent builds | 5 | 倉庫の他作品にダイアグラム主導は存在しない。AGENTS.md「未開拓 prefer」リストの「diagram / map / data-led」に直接当たる。 |

## Residual AI-ness / weaknesses (honest)
- **4×2 グリッドの整列**は最後まで残った。実物の編集物なら不規則配置や注釈の重ね打ちがあるはずで、placement 微オフセットだけでは消し切れていない。
- **凡例の説明文**(各 disc 下のキャプション)を全種に同じ書式で付けてしまった。Nightingale のように「ある disc にだけ長い説明が突き出る」非均一さは入れられなかった。
- **disc 中心の空白**が 8 種すべて同じ径で、ここも均質。本物の科学図なら disc によって中心円の意味が変わるはず。
- **時計の文字盤メタファー**そのものは強いが、当たり前すぎる。一覧性を捨てて「時刻軸を線条で延ばす」展開もあり得た。
- 初版にあった side-label (#4) はユーザ指摘で削除。代わりに「説明文の量を非均一化」を v0.2 で取り組むべき(下記)。
- 初版の METHOD ラベルと本文の被り(grid 設計ミス)もユーザ指摘で修正済。レンダー前の自己レビュー段階で気づけなかったのは反省点。

## Gate honesty check
- GATE 0 brief sign-off: yes (user OK, 時刻抽象化指示を反映)
- GATE 1 truly user-picked (not self-picked)? **yes** — AskUserQuestion で #2 を明示選択
- GATE 2 a real captured screenshot was observed (not from memory)? **yes** — `tools/rfm_shot.py` で取得、`reference_observation.md` は実際に画像を見て書いた

## One next change
- v0.2 でやるなら、**「全種同じキャプション書式」を捨てる**。ある 1 種だけ長文の観察記を付け、他はラベルだけ、というように「説明文の量」を非均一に。Nightingale が右の円にだけ全長の注を巻きつけているのと同じ手つき。
