# coding:utf-8

import os
#ログ制御用のコマンド定義
logCat = ' logcat '
clear = '-c'
logTime = '-v time -d > '
fileName = '/Log.txt'

def logClear(adbPath):
    #pcapFPath, exts = os.path.splitext(os.path.basename(apkFile))
    checkNum = 0
    cmd = adbPath + logCat + clear
    #print cmd
    checkNum += os.system(cmd)
    return checkNum



def getLogfile(adbPath, apkFile, pcapPath):
    checkNum = 0
    pcapFPath, exts = os.path.splitext(os.path.basename(apkFile))
    cmd = adbPath + logCat + logTime + pcapPath +pcapFPath + fileName
    cmd2 = 'mkdir ' + pcapPath + pcapFPath
    #print cmd2
    checkNum += os.system(cmd2)
    #print cmd
    checkNum += os.system(cmd)
    return checkNum