#coding:utf-8

import os
import time

#Vmのスナップショット名
vmSnapName = ['WhiteMain']

#vmスナップショットリストアコマンド
cmdRestore = ['VBoxManage snapshot "','" restore "','"']

def vmSnapRestore(vmName):
    checkNum = 0
    cmd = cmdRestore[0] + vmName + cmdRestore[1] + vmSnapName[0] + cmdRestore[2]
    print cmd
    checkNum = os.system(cmd)
    time.sleep(10)
    return checkNum