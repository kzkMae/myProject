# coding utf-8
import os

def x():
    return 0

#フォルダの有無を確認
def findFolderExist(folderName):
    folderExist = os.path.exists(folderName.lstrip('/'))
    if folderExist:
        return 0
    return 1


