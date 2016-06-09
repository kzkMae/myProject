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
            print '引数で指定されたフォルダは存在しません'
            return 1
    return 0
