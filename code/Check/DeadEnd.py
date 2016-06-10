# coding:utf-8
import sys
#このプログラムを強制的に終了させるための関数様々な状況下で実行可能にしておく

def deadErrorEnd(checkNumber):
    if not (checkNumber == 0):
        print '終了します'
        #print checkNumber
        sys.exit()
    return 0
