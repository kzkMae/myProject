# coding:utf-8
from Check.DeadEnd import *
from GUI.guiOperate import *
from apkGenymotion.executeAPK import *
from apkGenymotion.packetCapture import *
from vmReset.vmRestGeny import *

#Genymotionの起動（引数は仮想マシン名）
def startGenymotion(playerPath, vmName):
    #Genymotion起動のためのコマンドを作成
    startCommand = playerPath + ' --vm-name ' + vmName
    return 0

#Genymotinon操作のエラーチェック
def checkErrorGenymotion(checkNumber):
    #ErrorCheck
    deadErrorEnd(checkNumber)
    return 0

'''
#Genymotionを操作するメイン関数(playerファイルが実行できないため使用しない)
def operateGenymotionMain(apkName, vmName, playerPath):
    print apkName
    return 0
'''


#Genymotionを操作するメイン関数
def operateGenymotionMain(apkName, vmName, adbPath):
    print apkName
    #Genymotionをクリックして起動
    checkNumber = startGenymotionMain()
    #エラーのチェック
    deadErrorEnd(checkNumber)

    #解析用コマンド挿入
    #パケットキャプチャーソフトの起動
    checkNumber = packetCaptureStartMain(adbPath)
    #エラーのチェック
    deadErrorEnd(checkNumber)

    #ここから


    #パケットキャプチャーソフトの終了
    checkNumber = packetCaptureEndMain(adbPath)
    #エラーのチェック
    deadErrorEnd(checkNumber)

    #Genymotionをクリックして終了
    checkNumber = endGenymotionMain()
    #エラーのチェック
    deadErrorEnd(checkNumber)

    #VMをリストア
    checkNumber = vmSnapRestore(vmName)
    #エラーのチェック
    deadErrorEnd(checkNumber)
    return 0
