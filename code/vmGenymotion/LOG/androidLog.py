# conding:utf-8

import os
#ログ制御用のコマンド定義
logcat = ' logcat '
clear = '-c'
logtime = '-v time -d > '
fileName = '/Log.txt'

def logClear(adbPath):
    #pcapFPath, exts = os.path.splitext(os.path.basename(apkFile))
    checkNum = 0
    cmd = adbPath + logcat + clear
    checkNum += os.system(cmd)
    return checkNum



def getLogfile(adbPath, apkFile, pcapPath):
    checkNum = 0
    pcapFPath, exts = os.path.splitext(os.path.basename(apkFile))
    cmd = adbPath + logcat + logtime + pcapFPath + fileName
    checkNum += os.system(cmd)
    return checkNum