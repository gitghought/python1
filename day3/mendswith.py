
mstr = "u can u up, no can no 13 B"

#查看实现准备好的字符串是否以‘B’字符结尾
#该函数的返回值是布尔值
mbool = mstr.endswith("B")

print(mbool)

#查看实现准备好的字符串是否以‘B’字符结尾
#该方法指定了查找的范围，3-末尾
#该函数的返回值是布尔值
mbool = mstr.endswith("B", 3, mstr.__len__())
print(mbool)

