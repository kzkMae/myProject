# coding:utf-8

import os
#出力結果を得るためにはsubprocessをインポートする必要がある
import subprocess


#アプリのパッケージ名とメインアクティビティ名を取得する
def getPackegeName(apkName , aaptPath):
    cmd = aaptPath + ' l -a ' + apkName + ' | grep "A: package"'
    packagenameLine = subprocess.check_output([cmd], shell=True)
    packageName = packagenameLine.split('"')[1]
    print packageName
    return packageName

def getMainActivityName(apkName, aaptPath):
    cmd = aaptPath + ' d badging ' + apkName + ' | grep "activity"'
    mainactivitynameLine = subprocess.check_output([cmd], shell=True)
    mainactivityName = mainactivitynameLine.split('\'')[1]
    print mainactivityName
    return mainactivityName

def getExecuteCmd(packageName, activityName):
    executeCmd = packageName + '/.' + activityName.lstrip(packageName)
    return executeCmd

startCmd = ' shell am start -n '

def startAPKapp(adbPath, exeCmd):
    checkNum =0
    cmd = adbPath + startCmd + exeCmd
    print cmd
    checkNum += os.system(cmd)
    return checkNum

#アプリのインストール
def apkInstall(adbPath, apkName):
    checkNum = 0
    #インストール用のコマンド生成
    cmd = adbPath + ' install ' + apkName
    print cmd
    checkNum = os.system(cmd)
    return checkNum

#apkNameのGenymotionの中にインストールし実行するためのメイン関数
def executeAPKMain(apkName, adbPath, aaptPath):
    checkNum = 0
    #install
    checkNum += apkInstall(adbPath, apkName)
    packageName = getPackegeName(apkName,aaptPath)
    activityName = getMainActivityName(apkName,aaptPath)
    executeCommand = getExecuteCmd(packageName,activityName)
    checkNum += startAPKapp(adbPath, executeCommand)
    return checkNum