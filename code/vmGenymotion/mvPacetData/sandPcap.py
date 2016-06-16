#coding:utf-8

import os
import time

#Genymotion内のPcapが保存されているフォルダパス
genyPfolder = '/storage/emulated/legacy/Android/data/jp.taosoftware.android.packetcapture/files '
pullcmd = ' pull '


#PcapファイルをGenymotionからローカルフォルダに移動
def mvPcapFileMain(adbPath, pcapFolder, apkFile):
    checkNum = 0
    #移動コマンド生成(未完成)
    cmd = adbPath + pullcmd + genyPfolder
    #Apkファイル名からフォルダ名を生成（.apk拡張子を取り除く）
    pcapFPath, exts = os.path.splitext( os.path.basename(apkFile) )
    #移動コマンドを完成
    cmd += (pcapFolder + pcapFPath)
    #実行
    checkNum = os.system(cmd)
    time.sleep(1)
    return checkNum