# if __name__ == '__main__':
#     #两种创建列表的方式
#     mlist = list() # mlist = []
#     print(type(mlist))
#
#     #使用append在列表尾添加数据
#     mlist.append("班长")
#     print(mlist)
#
#     ##使用insert在列表指定位置添加数据
#     mlist.insert(0,"学委")
#     print(mlist)
#     #
#     # #根据数据来从列表中删除数据
#     # #   如果该数据不存在，则抛出异常
#     # #       ValueError: list.remove(x): x not in list
#     # mlist.remove("学")
#     # print(mlist)
#     #
#     # #删除整个列表
#     # del mlist
#     #
#     # #由于删除了整个列表，该对象不存在
#     # #   故不能再此处输出列表值
#     # print(mlist)
#
#
#     #使用pop从列表删除数据
#     #如果不指定参数，则删除列表中最后一个数据并返回
#     val = mlist.pop()
#     print("mlist.pop = {popval}".format(popval = val))
#
#     print(mlist)
#
#     #使用del从列表中删除数据
#     del mlist[0]
#
#     print(mlist)

# if __name__ == '__main__':
#     #创建两个列表
#     #尝试简单的列表间的赋值
#     mlist = [1,2,3]
#     nlist = mlist
#
#     #修改列表中一个值
#     # 注意观察两个列表中的值
#     nlist[0] = 3
#
#     print("nlist = {0}".format(nlist))
#     print("mlist = {0}".format(mlist))

if __name__ == '__main__':
    #创建两个列表
    #使用真正的列表复制
    mlist = [1,2,3]
    nlist = mlist[:]

    #修改列表中一个值
    # 注意观察两个列表中的值
    nlist[0] = 3

    print("nlist = {0}".format(nlist))
    print("mlist = {0}".format(mlist))
