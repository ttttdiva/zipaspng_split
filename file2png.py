import os
import shutil
import re
import argparse
import subprocess as subp
import random
from time import sleep
from zipaspng import disguise_file




# 埋め込み先画像フォルダ、一時フォルダ、埋め込み画像出力先フォルダを定義
base = r"F:/Macro/f_nk_out/zip-as-png-py/base/"
inputs = r"F:/Macro/f_nk_out/zip-as-png-py/inputs/"
outputs = r"F:/Macro/f_nk_out/zip-as-png-py/outputs/"
exe_file = r"C:\Program Files\7-Zip\7z.exe"

# 埋め込み先画像一覧を取得
inpngs = os.listdir(base)

# ファイルパス受け取り
parser = argparse.ArgumentParser()
parser.add_argument("--src",nargs="*")
args = parser.parse_args()

print(args.src)
print("Will embed " + str(len(args.src)) + "Files")


try:
    for x in range(len(args.src)):
        # 7zipで分割圧縮
        src_dirn = re.sub(r"\\","/",args.src[x]).split("/")[-1].replace("\"","")
        f_zip = inputs + src_dirn + ".zip"
        # 7z a --mx=0 v100m "input.zip" "input"
        cmd_l = (exe_file,"a","-mx=0","-v100m",f_zip,args.src[x])
        subp.run(cmd_l,shell=True)

        # 分割圧縮ファイル一覧を取得
        zips = os.listdir(inputs)

        for i in range(len(zips)):
            # 分割圧縮ファイルを再zip化
            f_zip = inputs + zips[i] + ".zip"
            cmd_l = (exe_file,"a","-mx=0",f_zip,inputs + zips[i])
            # 7z a --mx=0 "input.zip.001.zip" "input.zip.001"
            subp.run(cmd_l,shell=True)

            secretzip = f_zip
            embedding = base + random.choice(inpngs)
            # 分割圧縮時にできた.zipを-S7e4H1ln16-に置換
            outputimage = outputs + zips[i].replace(".zip","-S7e4H1ln16-") + ".png"
            while True:
                try:
                    # ZIPを画像に埋め込み
                    print(embedding)
                    # disguise_file(input.zip.001.zip, base.png, input-S7e4H1ln16-001.png)
                    disguise_file(secretzip, embedding, outputimage)
                    break
                except:
                    # 埋め込み先画像に既にZIPが埋め込まれているか問題がある。問題ないpngを引くまで再試行
                    os.remove(outputimage)
                    embedding = base + random.choice(inpngs)
        # 分割圧縮と再zip化ファイルをフォルダ毎削除＆フォルダ作成
        sleep(1)
        shutil.rmtree(inputs)
        os.mkdir(inputs)
        sleep(1)
except:
    # エラー出たらtraceback結果コピーして教えてください
    import traceback
    traceback.print_exc()
    input()
