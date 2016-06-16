# coding:utf-8

import os

#アプリのインストール
def apkInstall(adbPath, apkName):
    checkNum = 0
    #インストール用のコマンド生成
    cmd = adbPath + ' install ' + apkName
    print cmd
    #checkNum = os.system(cmd)
    return checkNum

#apkNameのGenymotionの中にインストールし実行するためのメイン関数
def executeAPKMain(apkName, adbPath, aaptPath):
    checkNum = 0
    #install
    checkNum += apkInstall(adbPath, apkName)
    return checkNum