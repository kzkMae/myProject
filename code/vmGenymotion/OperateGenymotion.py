# coding:utf-8
from Check.DeadEnd import *
from GUI.guiOperate import *
from apkGenymotion.executeAPK import *
from apkGenymotion.packetCapture import *
from vmReset.vmRestGeny import *
from mvPacetData.sandPcap import *
from LOG.androidLog import *


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
def operateGenymotionMain(apkName, vmName, adbPath, aaptPath, pcapFolder):
    print apkName
    #Genymotionをクリックして起動
    checkNumber = startGenymotionMain()
    #エラーのチェック
    deadErrorEnd(checkNumber)

    #解析用コマンド挿入
    #パケットキャプチャーソフトの起動
    checkNumber = packetCaptureStartMain(adbPath)
    #エラーのチェック
    deadErrorEnd2(checkNumber,vmName)

    #ログ情報をクリア
    checkNumber = logClear(adbPath)
    deadErrorEnd2(checkNumber,vmName)


    #APKファイルのインストールと実行
    checkNumber = executeAPKMain(apkName, adbPath, aaptPath)
    # エラーのチェック
    deadErrorEnd2(checkNumber,vmName)


    #60秒間パケットを記録
    for i in range(3):
        os.system(adbPath + ' shell input keyevent KEYCODE_DPAD_RIGHT')
        os.system(adbPath + ' shell input keyevent KEYCODE_ENTER')
        time.sleep(20)


    #パケットキャプチャーソフトの終了
    checkNumber = packetCaptureEndMain(adbPath)
    #エラーのチェック
    deadErrorEnd2(checkNumber,vmName)


    #ログ情報を保存
    checkNumber = getLogfile(adbPath, apkName, pcapFolder)
    #エラーのチェック
    deadErrorEnd2(checkNumber,vmName)


    #パケットキャプチャーソフトで作成したPcapファイルをローカルフォルダに移動する
    checkNum = mvPcapFileMain(adbPath, pcapFolder, apkName)


    #Genymotionをクリックして終了
    checkNumber = endGenymotionMain()
    #エラーのチェック
    deadErrorEnd2(checkNumber,vmName)

    #VMをリストア
    checkNumber = vmSnapRestore(vmName)
    #エラーのチェック
    deadErrorEnd(checkNumber)
    return 0
