# coding:utf-8
import os


#フォルダの有無を確認
def findFolderExist(folderName):
    folderExist = os.path.exists(folderName.lstrip('/'))
    if folderExist:
        return 0
    return 1


#引数に与えられた文字列のフォルダが存在するかを確認
def findFolderMain(apkFolder, adbFolder):
    folderList = [apkFolder, adbFolder]
    for i in range(len(folderList)):
        j = findFolderExist(folderList[i])
        if not (j == 0):
            print '引数で指定されたフォルダ('+folderList[i]+')は存在しません'
            return 1
    return 0

#adbフォルダ内にadbの実行ファイルがあるかを確認
def ADBfileExist(adbFolder):
    fileExist = os.path.isfile(adbFolder + 'adb')
    if fileExist:
        return 0
    print 'adbの実行ファイルが存在しないゾ☆'
    return 1

#adbファイルの絶対パスとエラーチェック用コードを返却する
def ADBfilePath(adbFolder):
    checkNum = ADBfileExist(adbFolder)
    return checkNum, adbFolder+'adb'

