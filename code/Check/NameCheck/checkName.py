# coding:utf-8

#vmNameListは事前に登録しておく仮想マシンの名前
#VMgenyはテスト用なので後で消すように
vmNameList = ['VMgeny']

#vmNameが（本ポログラムに）事前に登録されているものと一致するかどうかを確認
def checkVMname(vmName):
    for i in range(len(vmNameList)):
        if vmName == vmNameList[i]:
            print '仮想マシン名('+vmNameList[i]+')で解析するのね！'
            return 0
    print '仮想マシン名：'+vmName+'というVMは存在しないゾ☆'
    return 1