# coding:utf-8

#引数が文字列であるかどうかを調査
def checkargumentType(argMain):
    xtypeList = [argMain.apkFolder, argMain.adbFolder]
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


#引数の数と文字列かどうかを判定
def checkArgument(argMain):
    rx = 0
    rx += checkargumentType(argMain)
    rx += checkargumentEqual(argMain.apkFolder, argMain.adbFolder)
    return rx

