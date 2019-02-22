
#使用set来创建一个集合对象
#注意观察集合产生后的成员数量
mset = set("good luck")

# print(mset)


#创建mset集合对象
mset = {1,2,3,3,4,4,5}

#创建nset集合对象
nset = {7,9,8,3}

#将两个实现准备好的集合取并集
gset = nset | mset

# print(gset)

#将两个实现准备好的集合取交集
gset = nset & mset

print(gset)



#创建mset集合对象
mset = {1,2,3,3,4,4,5}

#创建nset集合对象
nset = {7,9,8,3,4}

#将两个实现准备好的集合取差集
#将nset中包含的mset去掉
gset = nset - mset

print(gset)

#创建mset集合对象
mset = {1,2,3,3,4,4,5}

#创建nset集合对象
nset = {7,9,8,3,4}

#将两个实现准备好的集合进行运算
#将两个集合的并集中的交集部分去掉
gset = nset ^ mset

print(gset)

#创建mset集合对象
mset = {1,2,3,3,4,4,5}

#对集合对象添加数据
#注意此处使用的是update方法
mset.update({99,88,77})
print(mset)


#创建mset集合对象
mset = {1,2,3,3,4,4,5}

#将3从mset集合中移除
#如果3在mset中不存在，程序会报错
mset.remove(3)
print(mset)

#创建mset集合对象
mset = {1,2,3,3,4,4,5}

#将100从mset集合中移除
#如果100在mset中不存在，程序不会报错
mset.discard(100)
print(mset)
