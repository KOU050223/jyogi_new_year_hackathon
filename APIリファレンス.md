# API リファレンス

### システム

- `width`, `height`<br>
  画面の幅と高さ

- `frame_count`<br>
  経過フレーム数

- `init(width, height, [title], [fps], [quit_key], [display_scale], [capture_scale], [capture_sec])`<br>
  Pyxel アプリケーションを画面サイズ (`width`, `height`) で初期化します。`title`でウィンドウタイトル、`fps`で動作フレームレート、`quit_key`でアプリケーション終了キー、`display_scale`で画面表示の倍率、`capture_scale`で画面キャプチャの倍率、`capture_sec`で画面キャプチャ動画の最大録画時間を指定します。<br>
  例：`pyxel.init(160, 120, title="My Pyxel App", fps=60, quit_key=pyxel.KEY_NONE, capture_scale=3, capture_sec=0)`

- `run(update, draw)`<br>
  Pyxel アプリケーションを開始し、フレーム更新時に`update`関数、描画時に`draw`関数を呼びます。

- `show()`<br>
  画面を表示し、`Esc`キーが押されるまで待機します。

- `flip()`<br>
  画面を 1 フレーム更新します。`Esc`を押すとアプリケーションは終了します。この関数は Web 版では動作しません。

- `quit()`<br>
  Pyxel アプリケーションを終了します。

### リソース

- `load(filename, [excl_images], [excl_tilemaps], [excl_sounds], [excl_musics])`<br>
  リソースファイル (.pyxres) を読み込みます。オプションに`True`を指定すると、そのリソースは読み込まれません。また、同名のパレットファイル (.pyxpal) がリソースファイルと同じ場所に存在する場合は、パレットの表示色も変更されます。パレットファイルは、表示色を改行区切りの 16 進数 (例：`1100FF`) で入力します。パレットファイルを使うことで Pyxel Editor の表示色も変更可能です。

- `user_data_dir(vendor_name, app_name)`<br>
  `vendor_name`と`app_name`から生成されたユーザーデータ保存用ディレクトリを返します。該当ディレクトリが存在しない場合は自動で作成されます。ハイスコアやゲームの進行状況の保存先として使用します。<br>
  例：`print(pyxel.user_data_dir("Takashi Kitao", "Pyxel Shooter"))`

### 入力

- `mouse_x`, `mouse_y`<br>
  現在のマウスカーソル座標

- `mouse_wheel`<br>
  現在のマウスホイールの値

- `btn(key)`<br>
  `key`が押されていたら`True`、押されていなければ`False`を返します。([キー定義一覧](../python/pyxel/__init__.pyi))

- `btnp(key, [hold], [repeat])`<br>
  そのフレームに`key`が押されたら`True`、押されなければ`False`を返します。`hold`と`repeat`を指定すると、`hold`フレーム以上ボタンを押し続けた時に`repeat`フレーム間隔で`True`が返ります。

- `btnr(key)`<br>
  そのフレームに`key`が離されたら`True`、離されなければ`False`を返します。

- `mouse(visible)`<br>
  `visible`が`True`ならマウスカーソルを表示し、`False`なら非表示にします。マウスカーソルが非表示でも座標は更新されます。

### グラフィックス

- `colors`<br>
  パレットの表示色リスト。表示色は 24 ビット数値で指定します。Python リストを直接代入・取得する場合は、`colors.from_list`と`colors.to_list`を使用してください。<br>
  例：`old_colors = pyxel.colors.to_list(); pyxel.colors.from_list([0x111111, 0x222222, 0x333333]); pyxel.colors[15] = 0x112233`

- `images`<br>
  イメージバンク (Image クラスのインスタンス) のリスト (0-2)<br>
  例：`pyxel.images[0].load(0, 0, "title.png")`

- `tilemaps`<br>
  タイルマップ (Tilemap クラスのインスタンス) のリスト (0-7)

- `clip(x, y, w, h)`<br>
  画面の描画領域を (`x`, `y`) から幅`w`、高さ`h`に設定します。`clip()`で描画領域を全画面にリセットします。

- `camera(x, y)`<br>
  画面の左上隅の座標を (`x`, `y`) に変更します。`camera()`で左上隅の座標を (`0`, `0`) にリセットします。

- `pal(col1, col2)`<br>
  描画時に色`col1`を`col2`に置き換えます。`pal()`で初期状態にリセットします。

- `dither(alpha)`<br>
  描画時にディザリング (擬似半透明) を適用します。`alpha`は`0.0`-`1.0`の範囲で設定し、`0.0`が透明、`1.0`が不透明になります。

- `cls(col)`<br>
  画面を色`col`でクリアします。

- `pget(x, y)`<br>
  (`x`, `y`) のピクセルの色を取得します。

- `pset(x, y, col)`<br>
  (`x`, `y`) に色`col`のピクセルを描画します。

- `line(x1, y1, x2, y2, col)`<br>
  色`col`の直線を (`x1`, `y1`)-(`x2`, `y2`) に描画します。

- `rect(x, y, w, h, col)`<br>
  幅`w`、高さ`h`、色`col`の矩形を (`x`, `y`) に描画します。

- `rectb(x, y, w, h, col)`<br>
  幅`w`、高さ`h`、色`col`の矩形の輪郭線を (`x`, `y`) に描画します。

- `circ(x, y, r, col)`<br>
  半径`r`、色`col`の円を (`x`, `y`) に描画します。

- `circb(x, y, r, col)`<br>
  半径`r`、色`col`の円の輪郭線を (`x`, `y`) に描画します。

- `elli(x, y, w, h, col)`<br>
  幅`w`、高さ`h`、色`col`の楕円を (`x`, `y`) に描画します。

- `ellib(x, y, w, h, col)`<br>
  幅`w`、高さ`h`、色`col`の楕円の輪郭線を (`x`, `y`) に描画します。

- `tri(x1, y1, x2, y2, x3, y3, col)`<br>
  頂点が (`x1`, `y1`)、(`x2`, `y2`)、(`x3`, `y3`)、色`col`の三角形を描画します。

- `trib(x1, y1, x2, y2, x3, y3, col)`<br>
  頂点が (`x1`, `y1`)、(`x2`, `y2`)、(`x3`, `y3`)、色`col`の三角形の輪郭線を描画します。

- `fill(x, y, col)`<br>
  (`x`, `y`) と同じ色でつながっている領域を色`col`で塗りつぶします。

- `blt(x, y, img, u, v, w, h, [colkey], [rotate], [scale])`<br>
  イメージバンク`img`(0-2) の (`u`, `v`) からサイズ (`w`, `h`) の領域を (`x`, `y`) にコピーします。`w`、`h`それぞれに負の値を設定すると水平、垂直方向に反転します。`colkey`に色を指定すると透明色として扱われます。`rotate`(度:Degree)、`scale`(1.0=100%)、またはその両方を指定すると対応する変換が適用されます。

<img src="images/blt_figure.png">

- `bltm(x, y, tm, u, v, w, h, [colkey], [rotate], [scale])`<br>
  タイルマップ`tm`(0-7) の (`u`, `v`) からサイズ (`w`, `h`) の領域を (`x`, `y`) にコピーします。`w`、`h`それぞれに負の値を設定すると水平、垂直方向に反転します。`colkey`に色を指定すると透明色として扱われます。`rotate`(度:Degree)、`scale`(1.0=100%)、またはその両方を指定すると対応する変換が適用されます。1 タイルのサイズは 8x8 ピクセルで、`(image_tx, image_ty)`のタプルとしてタイルマップに格納されています。

<img src="images/bltm_figure.png">

- `text(x, y, s, col)`<br>
  色`col`の文字列`s`を (`x`, `y`) に描画します。

### オーディオ

- `sounds`<br>
  サウンド (Sound クラスのインスタンス) のリスト (0-63)<br>
  例：`pyxel.sounds[0].speed = 60`

- `musics`<br>
  ミュージック (Music クラスのインスタンス) のリスト (0-7)

- `play(ch, snd, [tick], [loop], [resume])`<br>
  チャンネル`ch`(0-3) でサウンド`snd`(0-63) を再生します。`snd`がリストの場合、順に再生されます。再生開始位置は`tick`(1 tick = 1/120 秒) で指定できます。`loop`に`True`を指定するとループ再生します。再生終了後に以前の音に復帰させるには`resume`に`True`を指定します。

- `playm(msc, [tick], [loop])`<br>
  ミュージック`msc`(0-7) を再生します。再生開始位置は`tick`(1 tick = 1/120 秒) で指定できます。`loop`に`True`を指定するとループ再生します。

- `stop([ch])`<br>
  指定したチャンネル`ch`(0-3) の再生を停止します。`stop()`で全チャンネルの再生を停止します。

- `play_pos(ch)`<br>
  チャンネル`ch`(0-3) のサウンド再生位置を`(sound_no, note_no)`のタプルとして取得します。再生停止時は`None`を返します。

### 数学

- `ceil(x)`<br>
  `x`以上の最小の整数を返します。

- `floor(x)`<br>
  `x`以下の最大の整数を返します。

- `sgn(x)`<br>
  `x`が正の時に`1`、`0`の時に`0`、負の時に`-1`を返します。

- `sqrt(x)`<br>
  `x`の平方根を返します。

- `sin(deg)`<br>
  `deg`度 (Degree) の正弦を返します。

- `cos(deg)`<br>
  `deg`度 (Degree) の余弦を返します。

- `atan2(y, x)`<br>
  `y`/`x`の逆正接を度 (Degree) で返します。

- `rseed(seed)`<br>
  乱数生成器のシードを設定します。

- `rndi(a, b)`<br>
  `a`以上`b`以下のランダムな整数を返します。

- `rndf(a, b)`<br>
  `a`以上`b`以下のランダムな小数を返します。

- `nseed(seed)`<br>
  Perlin ノイズのシードを設定します。

- `noise(x, [y], [z])`<br>
  指定された座標の Perlin ノイズ値を返します。

### Image クラス

- `width`, `height`<br>
  イメージの幅と高さ

- `set(x, y, data)`<br>
  (`x`, `y`) に文字列のリストでイメージを設定します。<br>
  例：`pyxel.images[0].set(10, 10, ["0123", "4567", "89ab", "cdef"])`

- `load(x, y, filename)`<br>
  (`x`, `y`) に画像ファイル (PNG/GIF/JPEG) を読み込みます。

- `pget(x, y)`<br>
  (`x`, `y`) のピクセルの色を取得します。

- `pset(x, y, col)`<br>
  (`x`, `y`) に色`col`のピクセルを描画します。

### Tilemap クラス

- `width`, `height`<br>
  タイルマップの幅と高さ

- `imgsrc`<br>
  タイルマップが参照するイメージバンク(0-2)

- `set(x, y, data)`<br>
  (`x`, `y`) に文字列のリストでタイルマップを設定します。<br>
  例：`pyxel.tilemap(0).set(0, 0, ["0000 0100 a0b0", "0001 0101 a1b1"])`

- `load(x, y, filename, layer)`<br>
  (`x`, `y`) に TMX ファイル (Tiled Map File) から描画順が`layer`(0-) のレイヤーを読み込みます。

- `pget(x, y)`<br>
  (`x`, `y`) のタイルを取得します。タイルは`(image_tx, image_ty)`のタプルです。

- `pset(x, y, tile)`<br>
  (`x`, `y`) にタイルを設定します。タイルは`(image_tx, image_ty)`のタプルです。

### Sound クラス

- `notes`<br>
  音程 (0-127) のリスト。数値が大きいほど音程は高くなり、`33`で 'A2'(440Hz) になります。休符は`-1`です。

- `tones`<br>
  音色 (0:Triangle / 1:Square / 2:Pulse / 3:Noise) のリスト

- `volumes`<br>
  音量 (0-7) のリスト

- `effects`<br>
  エフェクト (0:None / 1:Slide / 2:Vibrato / 3:FadeOut / 4:Half-FadeOut / 5:Quarter-FadeOut) のリスト

- `speed`<br>
  再生速度。`1`が最も速く、数値が大きいほど再生速度は遅くなります。`120`で 1 音の長さが 1 秒になります。

- `set(notes, tones, volumes, effects, speed)`<br>
  文字列で音程、音色、音量、エフェクトを設定します。音色、音量、エフェクトの長さが音程より短い場合は、先頭から繰り返されます。

- `set_notes(notes)`<br>
  'CDEFGAB'+'#-'+'01234'または'R'の文字列で音程を設定します。大文字と小文字は区別されず、空白は無視されます。<br>
  例：`pyxel.sounds[0].set_notes("G2B-2D3R RF3F3F3")`

- `set_tones(tones)`<br>
  'TSPN'の文字列で音色を設定します。大文字と小文字は区別されず、空白は無視されます。<br>
  例：`pyxel.sounds[0].set_tones("TTSS PPPN")`

- `set_volumes(volumes)`<br>
  '01234567'の文字列で音量を設定します。大文字と小文字は区別されず、空白は無視されます。<br>
  例：`pyxel.sounds[0].set_volumes("7777 7531")`

- `set_effects(effects)`<br>
  'NSVFHQ'の文字列でエフェクトを設定します。大文字と小文字は区別されず、空白は無視されます。<br>
  例：`pyxel.sounds[0].set_effects("NFNF NVVS")`

### Music クラス

- `seqs`<br>
  サウンド (0-63) のリストをチャンネル数分連ねた 2 次元リスト

- `set(seq0, seq1, seq2, ...)`<br>
  チャンネルのサウンド (0-63) のリストを設定します。空リストを指定すると、そのチャンネルは再生に使用されません。<br>
  例：`pyxel.musics[0].set([0, 1], [], [3])`

### 上級者向け API

Pyxel には、ユーザーを混乱させる可能性や、使用に専門知識が必要といった理由から、このリファレンスには記載していない「上級者向け API」があります。

腕に覚えのある方は、[こちら](../python/pyxel/__init__.pyi)を手がかりに、あっと驚くような作品づくりに挑戦してみてください！
