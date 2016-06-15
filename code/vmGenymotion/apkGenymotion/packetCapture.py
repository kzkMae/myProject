# coding:utf-8

import os
from Check.DeadEnd import *

#パケットキャプチャーソフト用の動作

#グローバル関数
#ソフト起動用のコマンド
cmdCapS = ' shell am start -n jp.co.taosoftware.android.packetcapture/.PacketCaptureActivity'


#パケットキャプチャー開始
#インプットを取り付ける
def packetCaptureStart(adbFile):
    checkNum = 0
    print adbFile + cmdCapS
    checkNum = os.system(adbFile + cmdCapS)
    return checkNum

#パケットキャプチャーソフト起動のメイン関数
def packetCaptureStartMain(adbExeFile):
    #パケットキャプチャー起動
    checkNum = packetCaptureStart(adbExeFile)
    #ErrorCheck
    deadErrorEnd(checkNum)
    return checkNum
