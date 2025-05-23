# Pyxel

https://github.com/kitao/pyxel/blob/main/docs/README.ja.md

## 環境構築

https://qiita.com/shun_sakamoto/items/7944d0ac4d30edf91fde

仮想環境作成

```bash
python -m venv pyxel
```

ライブラリの共有

書き出し
```
pip freeze >  requirements.txt
```

インスト―ル
```
pip install -r requirements.txt
```

アクティベート

windows

```bash
.\pyxel\Scripts\activate
```

mac

```bash
source pyxel/bin/activate  
```

プログラム起動

```bash
py main.py
```

指定したディレクトリ内の変化を監視し、変化があった際に自動でプログラムを再実行

```bash
pyxel watch WATCH_DIR Pythonスクリプトファイル
```
```
pyxel watch ./SplatterUsako ./SplatterUsako/main.py
```

ディレクトリの監視は、Ctrl(Command)+Cで終了します。

## 8bit-bgm-generator起動

- 事前にリポジトリからファイルをダウンロード
- MIDIファイルを出力したい場合は`pip install mido`を実行しておく

https://github.com/shiromofufactory/8bit-bgm-generator

```bash
pyxel play ./8bit-bgm-generator-master/8bit-bgm-gen
```

# エディター起動

```bash
pyxel edit ./SplatterUsako/assets/usako
```

# デプロイ
1. ビルド
```
pyxel package SplatterUsako ./SplatterUsako/main.py
```

2. HTMLファイル作成
```
pyxel app2html SplatterUsako.pyxapp
```
3. コピー

windows
```
rm -rf index.html
copy SplatterUsako.html index.html
```

mac
```
rm -rf index.html
cp SplatterUsako.html index.html
```


デプロイ先(Pages)

https://kou050223.github.io/jyogi_new_year_hackathon/


## 参考サイト

[【Python / Pyxel】Webで遊べてSNSに共有できる，レトロゲームを作ってみた．](https://qiita.com/rwatanab1999/items/d5c0bb876f0b44cac2f0)
