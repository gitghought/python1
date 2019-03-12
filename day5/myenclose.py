
#定义函数（外部函数）
def mfunout(*args) :
    #数据缓冲，列表
    #使用数据缓冲列表将内部函数保存起来
    mret = []

    for i in args:
        #内部函数
        # 将传过来的每一个参数平方后返回
        def mfunin() :
            return i*i

        #将内部函数追加到数据缓冲列表中
        mret.append(mfunin)

    #将内部函数返回
    #形成了一个标准的闭包
    return mret

if __name__ == '__main__':
    mfuns = mfunout(1,2,3)
    for f in mfuns :
        print(f())


#定义函数（外部函数）
def mfunout2(*args) :
    #数据缓冲，列表
    #使用数据缓冲列表将内部函数保存起来
    mret = []

    for i in args:
        #内部函数
        # 将传过来的每一个参数平方后返回
        # 利用mfunmiddle缓存临时循环变量，
        # 注意该函数有参数，参数值就是循环变量
        def mfunmiddle(i) :

            #定义内部函数，
            # 该函数时闭包
            # 函数的返回值时外部函数循环变量
            def mfunin() :
                return i * i

            #返回内部函数，该函数保存外部函数的参数或变量
            return mfunin

        #将内部函数追加到数据缓冲列表中
        mret.append(mfunmiddle(i))

    #将内部函数返回
    #形成了一个标准的闭包
    return mret

if __name__ == '__main__':
    for f in mfunout2(1,2,3) :
        print(f())
