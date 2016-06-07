# coding:utf-8

#引数の数が妥当であるかを評価(6/7現在は２の引数である)
checkArgNum=2
def checkArgumentNum(argNum):
    if not (argNum == (checkArgNum+1)):
        return 1
    return 0


#引数の数と文字列かどうかを判定
def checkArgument(argMain):
    rx = 0
    rx += checkArgumentNum(len(argMain))
    return rx

