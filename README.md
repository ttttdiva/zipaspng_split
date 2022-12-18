## 用途

容量の大きいフォルダやファイルを100MBに分割し、好きなpngに埋め込む

zip-as-png-pyを丸々流用
https://github.com/yoshi389111/zip-as-png-py

file2png.py：ファイルをzip化しpngに埋め込む
png2file.py：分割したpngを元に戻す

## セットアップ

■ファイル
file2png.py：14～17行目　パスを適宜変更
png2file.py：9行目　パスを適宜変更

■パス
base：zipを埋め込む対象画像を入れる場所
inputs：分割zip、再zip等を一時的に置く場所
outputs：埋め込み画像を出力する場所
exe_file：7z.exeへの絶対パス(7zipにパスが通ってる場合は"7z"だけでも良い)

## 使い方

以下のような構文で利用可能

フォルダやファイルを埋め込み
```
python file2png.py --src "C:\DreamBooth\" "C:\Hypernetwork" "D:\riffusion-model-v1.ckpt"
```

戻す時
```
python png2file.py --src "C:\DreamBooth-S7e4H1ln16-.001.png" "C:\DreamBooth-S7e4H1ln16-.002.png" "C:\DreamBooth-S7e4H1ln16-.003.png"
```

## Asrユーザー向け

for_Asr_User内にスクリプト及びコマンド定義ファイルがあるので、コマンドIDを好きなホットキーに割り振り
ファイルを選択した状態でホットキーを押せば埋め込み・戻しが実行できる
※file2png.py、png2file.py、python.exeをそれぞれ絶対パスで書いてるため要書き換え

## その他

- 埋め込み先のpngファイルを追加して良い？
  - 良い。5000枚程度はあった方が被りづらくていい感じかもしれない。

- 埋め込み先の画像の最低サイズはある？
  - 無い。画像としての表示内容も変化しない。

- 100MBという制限がある？
  - 無い。デカすぎると怪しい為100MBにしているだけ。
  - 同じ補助チャンクに収める為2GB未満である必要はあるが37行目の-v100mを変えることで調整可能。

- 無圧縮である必要がある？
  - 無い。圧縮計算時間を短くするため。

- 分割圧縮ファイルをそのまま埋め込まず再圧縮してる理由は？
  - 多分分割は最後のファイルにしかEOCDが無いため取り出せなくなる
