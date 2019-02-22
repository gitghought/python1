
#创建一个非空字典
mdict = {"name":"good", "age":"18"}

#创建一个空字典
ndict = dict()

#查看mdict的数据类型
print(type(mdict))

#查看ndict的数据类型
print(type(ndict))


#创建一个非空字典
mdict = {"name":"good", "age":"18"}

#修改实现准备的字典
#注意使用的特点，类似于数组的使用
#但是下标改用了字符串，也就是key
mdict["addr"] = "Beijing-Haidian"

print(mdict)

#创建一个非空字典
mdict = {"name":"good", "age":"18"}

#修改实现准备的字典
#注意使用的特点，类似于数组的使用
#但是下标改用了字符串，也就是key
mdict["addr"] = "Beijing-Haidian"

print(mdict)

#删除字典中一个数据
del mdict["addr"]

print(mdict)

#删除字典
#删除字典后，字典对象就不能再使用，否则报错
del mdict

# print(mdict)


#创建一个非空字典
#key使用了元组
mdict = {"name":"good", "age":"18", ("addr"):"gun"}

print(mdict)

#创建一个非空字典
#key使用了元组
mdict = {"name":"good", "age":"18", ("addr"):"gun"}

#将字典mdict转换成一个字符串类型
mstrdict = str(mdict)

print(type(mstrdict))
print("mstrdict = ",mstrdict)


#创建一个非空字典
#key使用了元组
mdict = {"name":"good", "age":"18", ("addr"):"gun"}

#求字典的长度
dictlen = len(mdict)

print(dictlen)

#创建一个非空字典
#key使用了元组
mdict = {"name":"good", "age":"18", ("addr"):"gun"}

#获取mdict的数据类型
mtype = type(mdict)

print(mtype)

