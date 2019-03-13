
# #如果for循环中没有任何语句，程序运行就报错
# for i in range(10):
#     pass
#
# #为了能够在空语句的for循环中正确执行，使用pass站位
# for i in range(10):
#     pass

# import random
# import time
#
# if __name__ == '__main__':
#     #设置当前随机数的种子
#     #在调用随机数方法前调用该函数
#     #如果种子的值固定不变，则随机数产生的值也不变
#     random.seed(10)
#     print(random.randint(1,10))

# import random
# import time
#
# if __name__ == '__main__':
#     #设置当前随机数的种子
#     #在调用随机数方法前调用该函数
#     #使用了当前系统的时间
#     #   故产生的随机值每次都不同
#     random.seed(time.time())
#     print(random.randint(1,10))


if __name__ == '__main__':
    #准备程序中使用的数据源
    mlist = [1,2,3]
    nlist = ["hoho","hehe", "hehe", "hoho"]

    #统计列表中指定数据的个数
    num = nlist.count("hehe")

    print(num)



