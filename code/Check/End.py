# coding:utf-8

#引数が文字列であるかどうかを調査
def checkargumentType(argMain):
    xtype = argMain.apkFolder
    ytype = argMain.adbFolder
    if xtype.isdigit() or ytype.isdigit():
        return 1
    return 0

#引数の数と文字列かどうかを判定
def checkArgument(argMain):
    rx = 0
    rx += checkargumentType(argMain)
    return rx

