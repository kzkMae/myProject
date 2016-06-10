# coding:utf-8
import glob

#APKフォルダ内にapkファイルがあるか否かを確認
def apkFileExist(listSize):
    if listSize == 0:
        #APKファイルが１つも存在しない
        print 'APKファイルが１つもないんだゾ☆'
        return 1
    #listSizeの中身があればエラーなし
    return 0



#APKファイルをリストで受け取る
#返却値には，Checkコード，ファイルリスト，サイズ
def getAPKfileList(apkFolder):
    apkList = glob.glob(apkFolder+'*.apk')
    #apkListのサイズを求める
    apkListSize = len(apkList)
    #apkListの中身があるかを確認
    checkNum = apkFileExist(apkListSize)
    return checkNum, apkList, apkListSize

