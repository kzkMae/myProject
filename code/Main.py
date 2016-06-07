# coding:utf-8
#メイン関数
#全ての起点

#import文で使用するパッケージを指定
#
import sys
from Check.End import *



#自分で作成したファイルをインポート

#引数を定義
#１．APKファイルを保存しているPath
#２．Adbファイルを保存しているPath
#３．
arguMain = sys.argv

#引数の数でエラー表示
arguMainNum = len(arguMain)

checkNum = checkArgument(arguMain)
if not (checkNum == 0):
    print '終了します'
    #print checkNum
    sys.exit()


#APKファイル保存フォルダPath
apkFileFpath = arguMain[1]
#print apkFileFpath

#Adbファイル保存フォルダPath
adbFileFpath = arguMain[2]
#print adbFileFpath

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




