
mstr = "u can u up, no zuo no die"

#查看实现准备好的字符串是否以‘u’字符开头
#该函数的返回值是布尔值
mbool = mstr.startswith("u")

print(mbool)

#查看实现准备好的字符串是否在2-4的范围内以‘c’字符开头
#注意该函数指定了查找的范围
#该函数的返回值是布尔值
mbool = mstr.startswith("c", 2, 4)

print(mbool)