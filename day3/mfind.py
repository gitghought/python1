
mstr = "good good study , day day up"

#在源字符串中查找“good”子字符串
#该函数返回找到的子字符串的起始下标
mindex = mstr.find("good")
print(mindex)


#在源字符串中查找“good”子字符串
#指定了从源字符串的起始下标1开始执行查找
#该函数返回找到的子字符串的起始下标
mindex = mstr.find("good", 1)
print(mindex)

#在源字符串中查找“good”子字符串
#指定了从源字符串的起始下标1开始执行查找
#指定了到源字符串10结束本次查找
#该函数返回找到的子字符串的起始下标
mindex = mstr.find("good", 1, 10)
print(mindex)


