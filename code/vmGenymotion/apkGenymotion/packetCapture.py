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
swipe = ' shell input swipe '
tap = ' shell input tap '

#パケットキャプチャー開始
#インプットを取り付ける
def packetCaptureStart(adbFile):
    checkNum = 0
    #print adbFile + cmdCapS
    checkNum += os.system(adbFile + cmdCapS)
    time.sleep(timesec[0])
    for i in range(3):
        cmd = adbFile + keyevent +'KEYCODE_DPAD_DOWN'
        checkNum += os.system(cmd)
        time.sleep(timesec[1])
    cmdE = adbFile + keyevent + 'KEYCODE_ENTER'
    checkNum += os.system(cmdE)
    time.sleep(timesec[2])
    checkNum += os.system(cmdE)
    time.sleep(timesec[2])

    cmd = adbFile + keyevent + 'KEYCODE_DPAD_RIGHT'
    checkNum += os.system(cmd)
    time.sleep(timesec[2])
    checkNum += os.system(cmdE)
    time.sleep(timesec[2])

    cmd = adbFile + keyevent + 'KEYCODE_HOME'
    checkNum += os.system(cmd)
    time.sleep(timesec[0])
    return checkNum

#パケットキャプチャーソフト起動のメイン関数
def packetCaptureStartMain(adbExeFile):
    #パケットキャプチャー起動
    checkNum = packetCaptureStart(adbExeFile)
    #ErrorCheck
    deadErrorEnd(checkNum)
    time.sleep(timesec[0])
    return checkNum


def packetCaptureEnd(adbFile):
    checkNum =0
    cmd = adbFile + keyevent + 'KEYCODE_HOME'
    checkNum += os.system(cmd)
    time.sleep(timesec[0])
    #スワイプ
    cmd = adbFile + swipe + '10 20 10 1000'
    checkNum += os.system(cmd)
    time.sleep(timesec[2])
    #タップ
    cmd = adbFile + tap + '300 150'
    checkNum += os.system(cmd)
    time.sleep(timesec[2])
    #キャプチャー停止
    cmd = adbFile + keyevent + 'KEYCODE_DPAD_RIGHT'
    checkNum += os.system(cmd)
    time.sleep(timesec[1])
    checkNum += os.system(cmd)
    time.sleep(timesec[1])
    cmd = adbFile + keyevent + 'KEYCODE_ENTER'
    checkNum += os.system(cmd)
    time.sleep(timesec[1])
    return checkNum


def packetCaptureEndMain(adbExeFile):
    checkNum = 0
    #パケットキャプチャー終了
    checkNum = packetCaptureEnd(adbExeFile)
    #ErrorCheck
    deadErrorEnd(checkNum)
    time.sleep(timesec[0])
    return checkNum