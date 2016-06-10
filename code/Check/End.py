# coding:utf-8
import os.path

#名前をチェックするのに使用するファイルと関数
from NameCheck.checkName import *


#引数が文字列であるかどうかを調査
def checkargumentType(argMain):
    xtypeList = [argMain.apkFolder, argMain.adbFolder, argMain.vmName]
    for i in range(len(xtypeList)):
        if xtypeList[i].isdigit():
            print '数字として処理できてしまう'
            return 1
    return 0



#入力された値が同じであるか否かを判定
def checkargumentEqual(apkFolder, adbFolder):
    if apkFolder == adbFolder:
        print '違うフォルダを指定してください'
        return 1
    return 0


#「/」で始まり，「/」で終わっているか→フォルダを指定しているか
def checkargumentFolder(apkFolder, adbFolder):
    #if not (apkFolder.startswith('/') and adbFolder.startswith('/')):
    if not (os.path.isabs(apkFolder) and os.path.isabs(adbFolder)):
        #print '「/」で始めてください'
        print '絶対パスを指定してください'
        return 1
    if not (apkFolder.endswith('/') and adbFolder.endswith('/')):
        print '「/」で終わってください'
        return 1
    return 0


#vmNameに対する確認関数
def checkargumentVMName(VMname):
    if not (checkVMname(VMname) == 0):
        print '登録している仮想マシン名を入力するのだゾ☆'
        print '新しく'+VMname+'を登録するのもOK！！'
        return 1
    return 0

#引数の数と文字列かどうかを判定
def checkArgument(argMain):
    rx = 0
    #引数の型を確認
    rx += checkargumentType(argMain)
    #フォルダが同じでないことを確認
    rx += checkargumentEqual(argMain.apkFolder, argMain.adbFolder)
    #絶対パスであり，「/」で終わっていることを確認
    rx += checkargumentFolder(argMain.apkFolder, argMain.adbFolder)
    #vmNameに対する確認
    rx += checkargumentVMName(argMain.vmName)
    return rx

