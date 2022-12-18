import os
import re
import argparse
import subprocess as subp
from time import sleep


# 7zipのパス指定
exe_file = r"C:\Program Files\7-Zip\7z.exe"

# ファイルパス受け取り
parser = argparse.ArgumentParser()
parser.add_argument("--src",nargs="*")
args = parser.parse_args()

l_png1 = [re.sub("\.\d\d\d\.png$","",i) for i in args.src]
l_png2 = list(set(l_png1))

print(l_png2)
print("Will unzip " + str(len(l_png2)) + "Zips")

szip_list = []

try:
    for y in l_png2:
        xl_png = [s for s in args.src if y in s]
        for x in xl_png:
            srcfile = re.sub(r"\\","/",x).split("/")[-1].replace("\"","")
            srcdir = x.replace(srcfile,"")
            mvsrcfile = srcfile.replace("-S7e4H1ln16-",".zip").replace(".png",".zip")
            szip_list.append(srcdir + re.sub(".zip$","",mvsrcfile))
            
            # ファイル名をzipに戻す
            os.rename(srcdir + srcfile,srcdir + mvsrcfile)

            # 7zipで解凍(分割圧縮に戻す)
            cmd_l = (exe_file,"x",srcdir + mvsrcfile)
            subp.run(cmd_l,shell=True)
        
        # 分割圧縮zipを結合
        szipstr = "\"" + "\"+\"".join(szip_list) + "\""
        cmd_l = "copy /b " + szipstr + " output.zip"
        subp.run(cmd_l,shell=True)

        # zipを解凍
        cmd_l = (exe_file,"x","output.zip")
        subp.run(cmd_l,shell=True)

        # 元の分割圧縮zipや結合zip等を削除
        for i in szip_list:
            print(i)
            os.remove(i)
            os.remove(i + ".zip")
        os.remove(srcdir + "output.zip")
        szip_list = []

except:
    # 今のところエラー出たこと無いが一応
    import traceback
    traceback.print_exc()
    input()
