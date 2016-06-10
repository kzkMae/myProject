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
#引数をもとに指定のフォルダを見つける
from Find.FindFolder import *

#引数や-hのオプションを定義
parser = argparse.ArgumentParser(prog='Run_ApkFile_in_Genymotion',description='オプションと引数の説明',
                                epilog='以上')

parser.add_argument('apkFolder',type=str, help='Apkファイルを保存しているフォルダを指定, 型：%(type)s')
parser.add_argument('adbFolder',type=str,help='GenymotionのAdbファイルが保存しているフォルダを指定, 型：%(type)s')
parser.add_argument('-v','--version', action='version', version='%(prog)s version 6/8')

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


checkNum = findFolderMain(apkFileFpath, adbFileFpath)
#ErrorCheck
deadErrorEnd(checkNum)


#ADBの実行ファイルの絶対パスを取得
checkNum, adbPath = ADBfilePath(adbFileFpath)
#ErrorCheck
deadErrorEnd(checkNum)

#testCode(最終的には外す or コメントアウト)
print '無問題'


#APKを保存しているPathからAPKファイルのリストを作成


#以下，繰り返し

#Genymotionを起動




#パケットキャプチャーツールを起動



#GenymotionにAPKファイルをインストール



#パケットキャプチャーを停止



#パケットキャプチャーしたファイルを共有フォルダに移動



#共有フォルダからPcapファイルを取り出す


#Genymotionを停止



#VirtualBoxをスナップショットから復元


#APKファイルをSHA256を計算


#VirsuTotalにSHA256を投げる


#繰り返し終わり




