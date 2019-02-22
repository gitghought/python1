
import random

#choice 方法用于从已经给定的序列中随机选择一个数值
v = random.choice(range(10))
print(v)

#定义一个字符串，是字符的来源
mstr = "abcdefghijklmnopqrstuvwxyz"

#定义一个缓存字符的变量
tstr = ""

#循环5次
for i in range(5):
    #每一次循环就从源字符串中取出一个字符
    #并将取出的字符存储到临时追加并存储到变量tstr中
    tstr += random.choice(mstr)
    print(i, tstr)



#规定当前随机数使用的种子为10
#如果种子的值是固定的，则随机数产生的数值也是固定的
random.seed(10)
#在事先指定了种子的条件下，产生一个随机值
#注意每次产生的随机值都是一样的
v = random.random()
print(v)


#导入日期时间对应的包
import datetime

#使用时间的秒值作为种子
#因为每秒的数值都不同，所以种子的值就不同
#因此每次产生的随机值不同（在一分钟之内）
random.seed(datetime.time.second)

#在事先指定了种子的条件下，产生一个随机值
#注意每次产生的随机值在一分钟之内是不同的
v = random.random()
print(v)


#在1到10范围内生成随机数值
v = random.randrange(1,10)
print(v)

mlist = [1,9,8,5,4,3]

#每次对指定的列表执行随机打乱顺序
#注意每次执行，都是对原列表操作
#另外，列表中数值总是不同的
random.shuffle(mlist)
print(mlist)

#在3到4的范围内随机生成浮点数
v = random.uniform(3,4)
print(v)
