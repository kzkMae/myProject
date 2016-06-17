# coding:utf-8
#メイン関数
#全ての起点

#import文で使用するパッケージを指定
#
import sys
#プログラムに余裕がある場合に実装
import argparse

#自分で作成したファイルをインポート
#入力した引数のチェック
from Check.End import *
from Check.DeadEnd import *
#引数をもとに指定のフォルダ・ファイルを見つける
from Find.FindFolder import *
from Find.FindAPKFile import *
#Genymotion操作用の関数
from vmGenymotion.OperateGenymotion import *

#引数や-hのオプションを定義
parser = argparse.ArgumentParser(prog='Run_ApkFile_in_Genymotion',description='オプションと引数の説明',
                                epilog='以上')

parser.add_argument('apkFolder',type=str, help='Apkファイルを保存しているフォルダを指定, 型：%(type)s，String')
parser.add_argument('adbFolder',type=str,help='GenymotionのAdbファイルが保存しているフォルダを指定, 型：%(type)s，String')
parser.add_argument('-v','--version', action='version', version='%(prog)s version 6/15')
parser.add_argument('vmName', type=str, help='Genumotionで起動する仮想マシン名(VM Name)を指定，型：%(type)s，String')
parser.add_argument('pcapFolder',type=str, help='パケットキャプチャーした後のPcapデータを保存するフォルダ，型：%(type)s, String')

#args = parser.parse_args()

#変数の定義
#エラーをチェック
checkNum = 0

#引数を定義
#１．APKファイルを保存しているPath
#２．Adbファイルを保存しているPath
#３．
#arguMain = sys.argv
arguMain = parser.parse_args()

#引数のエラー表示
checkNum = checkArgument(arguMain)
#ErrorCheck
deadErrorEnd(checkNum)

#APKファイル保存フォルダPath
apkFileFpath = arguMain.apkFolder
#print apkFileFpath

#Adbファイル保存フォルダPath
adbFileFpath = arguMain.adbFolder
#print adbFileFpath

#Pcapフォルダを保存するフォルダパス
pcapFolderPath = arguMain.pcapFolder


#フォルダが存在するかを確認
checkNum = findFolderMain(apkFileFpath, adbFileFpath)
#ErrorCheck
deadErrorEnd(checkNum)


#ADBの実行ファイルの絶対パスを取得
checkNum, adbPath = ADBfilePath(adbFileFpath)
#ErrorCheck
deadErrorEnd(checkNum)


#AAPTの実行ファイルの絶対パスを取得
checkNum, aaptPath = AAPTfilePath(adbFileFpath)
#ErrorCheck
deadErrorEnd(checkNum)



#APKを保存しているPathからAPKファイルのリストを作成
checkNum, apkFileList, apkFileNumber = getAPKfileList(apkFileFpath)
#ErrorCheck
deadErrorEnd(checkNum)

'''
#Genymotion起動用実行ファイルのパスを取得
checkNum, playerPath = PLAYERfilePath(adbFileFpath)
#ErrorCheck
deadErrorEnd(checkNum)
'''

#仮想マシンの名前
genymotionVMname = arguMain.vmName



#以下，繰り返し
for i in range(apkFileNumber):
    #print i
    apkFilePath = apkFileList[i]
    #Genymotionを起動
    print 'Genymotion起動'
    checkNum = operateGenymotionMain(apkFilePath, genymotionVMname, adbPath, aaptPath, pcapFolderPath)
    #ErrorCheck
    deadErrorEnd(checkNum)




#testCode(最終的には外す or コメントアウト)

print '無問題'





#GenymotionにAPKファイルをインストール



#APKファイルをSHA256を計算


#VirsuTotalにSHA256を投げる


#繰り返し終わり




