# #导入随机数生成器用到的包
# import random
#
# if __name__ == '__main__':
    # #随机从给定范围取一个整数
    # val = random.randint(1,2)
    # print(val)
    #
    # #从给定序列中随机选择一个数
    # val = random.choice(range(3))
    # print("val = {val}".format(val = val))

    # #数据源
    # mstr = "abcdefghijklmnopqrstuvwxyz"
    #
    # #临时存储变量
    # tstr = ""
    #
    # #循环三次，相当于控制循环次数，从数据源中取出三个字符
    # for i in range(3) :
    #     #随机从数据源中取出一个字符
    #     v = random.choice(mstr)
    #
    #     #追加到临时变量
    #     tstr += v
    #
    # print(tstr)

# # 导入随机数生成器用到的包
# import random
#
# if __name__ == '__main__':
#     #从0到9随机生成一个整数
#     rval = random.randrange(0,10,1)
#
#     print("val = {rval}".format(rval = rval))


# 导入随机数生成器用到的包
import random

if __name__ == '__main__':
    #数据源
    mstrs = ["hehe", "hoho", "heihei"]

    #打印打乱顺序前的数据源
    print("before {0}".format(mstrs))

    #对数据源执行顺序打乱
    random.shuffle(mstrs)

    #打印打乱顺序后的数据源
    print("after {0}".format(mstrs))

    print(random.uniform(3,4))

    random.randrange()


