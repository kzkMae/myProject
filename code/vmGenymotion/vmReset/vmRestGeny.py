#coding:utf-8

import os
import time

#Vmのスナップショット名
vmSnapName = ['WhiteExe']

#vmスナップショットリストアコマンド
cmdRestore = ['VBoxManage snapshot "','" restorecurrent']

def vmSnapRestore():
    checkNum = 0
    cmd = cmdRestore[0] + vmSnapName[0] + cmdRestore[1]
    print cmd
    checkNum = os.system(cmd)
    time.sleep(10)
    return checkNum