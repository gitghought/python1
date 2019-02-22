
mstr = "good good study , day day up"

#在源字符串中统计“good”子字符串的次数
#该函数返回找到的子字符串的数量
mcount = mstr.count("good")
print(mcount)

#在源字符串中统计“good”子字符串的数量
#指定了从源字符串的起始下标1开始执行计数
#该函数返回找到的子字符串的数量
mcount = mstr.count("good", 1)
print(mcount)

#在源字符串中查找“good”子字符串
#指定了从源字符串的起始下标1开始执行计数
#指定了到源字符串10结束本次计数
#该函数返回找到的子字符串的数量
mcount = mstr.count("good", 1, 10)
print(mcount)