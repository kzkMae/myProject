# coding:utf-8

import os
import time
from Check.DeadEnd import *

#パケットキャプチャーソフト用の動作

#グローバル関数
#ソフト起動用のコマンド
timesec = [2,0.2,0.5]
cmdCapS = ' shell am start -n jp.co.taosoftware.android.packetcapture/.PacketCaptureActivity'
keyevent = ' shell input keyevent '

#パケットキャプチャー開始
#インプットを取り付ける
def packetCaptureStart(adbFile):
    checkNum = 0
    print adbFile + cmdCapS
    #checkNum += os.system(adbFile + cmdCapS)
    time.sleep(timesec[0])
    for i in range(3):
        cmd = adbFile + keyevent +'KEYCODE_DPAD_DOWN'
        print cmd
        #checkNum += os.system(cmd)
        time.sleep(timesec[1])
    cmd = adbFile + keyevent + 'KEYCODE_ENTER'
    print cmd
    #checkNum += os.system(cmd)
    time.sleep(timesec[2])
    #checkNum += os.system(cmd)
    time.sleep(timesec[2])
    return checkNum

#パケットキャプチャーソフト起動のメイン関数
def packetCaptureStartMain(adbExeFile):
    #パケットキャプチャー起動
    checkNum = packetCaptureStart(adbExeFile)
    #ErrorCheck
    deadErrorEnd(checkNum)
    time.sleep(timesec[0])
    return checkNum
