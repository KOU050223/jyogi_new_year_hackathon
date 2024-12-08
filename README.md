# Pyxel

https://github.com/kitao/pyxel/blob/main/docs/README.ja.md

## 環境構築

https://qiita.com/shun_sakamoto/items/7944d0ac4d30edf91fde

仮想環境作成

```bash
python -m venv pyxel
```

アクティベート

```bash
.\pyxel\Scripts\activate
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
pyxel watch . main.py
```

ディレクトリの監視は、Ctrl(Command)+Cで終了します。

## 8bit-bgm-generator起動

- 事前にリポジトリからファイルをダウンロード
- MIDIファイルを出力したい場合は`pip install mido`を実行しておく

https://github.com/shiromofufactory/8bit-bgm-generator

```bash
cd 8bit-bgm-generator-master
pyxel play 8bit-bgm-gen
```

## 参考サイト

[【Python / Pyxel】Webで遊べてSNSに共有できる，レトロゲームを作ってみた．](https://qiita.com/rwatanab1999/items/d5c0bb876f0b44cac2f0)
