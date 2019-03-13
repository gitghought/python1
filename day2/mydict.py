# if __name__ == '__main__':
#     mdict = {"name":"good", "password":"123"}
#
#     print(type(mdict))
#
#     #这种遍历字典的方式，取出的数据是字典中每一个键
#     for kv in mdict :
#         #显示的类型为str
#         # print(" type is {0} ".format(type(kv)))
#         print(kv)

# if __name__ == '__main__':
#     mdict = {"name":"good", "password":"123", "age":18}
#
#     print(type(mdict))
#
#     #这种遍历字典的方式，取出的数据是字典中每一个键
#     for k in mdict :
#         #显示的类型为str
#         # print(" type is {0} ".format(type(kv)))
#         # print(k)
#         print("mdict[{key}]={mdictval}".format(key = k, mdictval = mdict[k]))


#

if __name__ == '__main__':
    mdict = {"name":"good", "password":"123", "age":18}

    print(type(mdict))

    #这种遍历字典的方式，取出的数据是字典中每一个键值对
    for k,v in mdict.items() :
        print("mdict[{key}]={mdictval}".format(key = k, mdictval = v))



