# if __name__ == '__main__':
#     # for (i = 0; i < 3; i++) //java 中类似于range的代码实现
#     # 实现for循环3次
#     for i in range(3) :
#         if i == 2 :
#             break
#         print(i)

# if __name__ == '__main__':
#     # for (i = 0; i < 10; i+=2) //java 中类似于range的代码实现
#     # 实现for循环5次,步长为2
#     for i in range(0,10,2) :
#         print(i)

if __name__ == '__main__':
    #使用range初始化一个列表
    #第一个参数小于第二个参数时，第三个参数为正数
    mlist = [ i for i in range(0,10,1) ]
    print(mlist)

    #使用range初始化一个列表
    #第二个参数小于第一个参数时，第三个参数为负数
    mlist = [ i for i in range(10,1,-1) ]

    print(mlist)
