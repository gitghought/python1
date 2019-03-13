if __name__ == '__main__':
    mlist = [1,2,3,4]

    nlist = mlist

    #输出两个列表的id值
    #判断它们是否是同一个对象或变量
    print("mlist id is {mlistid}".format(mlistid = id(mlist)))
    print("nlist id is {nlistid}".format(nlistid = id(nlist)))
