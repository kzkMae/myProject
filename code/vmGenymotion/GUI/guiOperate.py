# coding:utf-8

import os
import time

#GUiでGenyotionの起動・停止を行うためのソースコード

#基本的には「xte」コマンドを用いる

#画面の位置を変数化
#Genymotionのスタートボタン，絶対位置（x,y）
startGeny = ['114','133']
#Genymotionの修了ボタン(x,y)
endGeny = ['642','45']
#Wait時間(起動直後)
waiTime = [0.5,5]
#xteコマンド(基礎)
xte = 'xte '
#xteコマンドの中身用
sq = '\''

mouseMove = 'mousemove '
mouseLClick = 'mouseclick 1'
cmd_c = xte + sq + mouseLClick + sq

#Genymotion起動
def startGenymotionClick():
    checkNum = 0
    startXY = startGeny[0] + ' ' + startGeny[1]
    #コマンド作成
    cmd_m = xte + sq + mouseMove + startXY + sq
    #cmd_c = xte + sq + mouseLClick + sq
    print cmd_m
    #checkNum += os.system(cmd_m)
    time.sleep(waiTime[0])
    print cmd_c
    #checkNum += os.system(cmd_c)
    #5秒間停止
    time.sleep(waiTime[1])
    return checkNum


#Genymotion終了
def endGenymotionClick():
    checkNum = 0
    endXY = endGeny[0] + ' ' + endGeny[1]
    #コマンド作成
    cmd_m = xte + sq + mouseMove + endXY + sq
    #cmd_c = xte + sq + mouseLClick + sq
    print cmd_m
    #checkNum += os.system(cmd_m)
    time.sleep(waiTime[0])
    print cmd_c
    #checkNum += os.system(cmd_c)
    #5秒間停止
    time.sleep(waiTime[1])
    return checkNum


#Genymotionを起動するMainの関数
def startGenymotionMain():
    checkNum = startGenymotionClick()
    return checkNum

def endGenymotionMain():
    checkNum = endGenymotionClick()
    return checkNum