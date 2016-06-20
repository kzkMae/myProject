# coding:utf-8
import sys
#このプログラムを強制的に終了させるための関数様々な状況下で実行可能にしておく

def deadErrorEnd(checkNumber):
    if not (checkNumber == 0):
        print '終了します'
        #print checkNumber
        sys.exit()
    return 0


import os
import time

#画面の位置を変数化
#Genymotionの修了ボタン，絶対位置(x,y)
endGeny = ['642','45']
#xteコマンド(基礎)
xte = 'xte '
#xteコマンドの中身用
sq = '\''

mouseMove = 'mousemove '
mouseLClick = 'mouseclick 1'
cmd_c = xte + sq + mouseLClick + sq

#Vmのスナップショット名
vmSnapName = ['WhiteExe']
#vmスナップショットリストアコマンド
cmdRestore = ['VBoxManage snapshot "','" restore "','"']

#Genymotion操作中のエラーの場合の終了手順
def deadErrorEnd2(checkNumber, vmName):
    if not (checkNumber == 0):
        #Genymotionの終了
        print 'Genymotionを強制終了します'
        endXY = endGeny[0] + ' ' + endGeny[1]
        cmd_m = xte + sq + mouseMove + endXY + sq
        #クリックで終了
        os.system(cmd_m)
        time.sleep(0.5)
        os.system(cmd_c)
        time.sleep(5)
        #Genymotionのスナップショットをリストア
        print 'スナップショットを強制復元します'
        cmd = cmdRestore[0] + vmName + cmdRestore[1] + vmSnapName[0] + cmdRestore[2]
        os.system(cmd)
        time.sleep(2)
        sys.exit()
    return 0