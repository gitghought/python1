mstr = "good good study , day day up"

#在源字符串中按照空格分割字符串
#该函数返回分割后的字符串列表
mlist = mstr.split(" ")

#打印新字符串到终端
print(mlist)

#在源字符串中按照空格分割字符串
#注意只对该字符串分割一次
#该函数返回分割后的字符串列表
nlist = mstr.split(" ", 1)
print(nlist)
