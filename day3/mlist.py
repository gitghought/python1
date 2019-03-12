


#创建一个源数据列表，
# 注意这是嵌套列表或者称为双层列表
mlist = [ ['a','b'], ['e','f'], ['g','h'] ]

#通过遍历的方式创建一个新的列表
# 数据来自源数据列表
# 注意输出的结果
nlist = [ [m,n]  for m,n in mlist]

print(nlist)

#定义一个字典
mlanguage = {"j":"java", "c":"c", "p":"python"}

#按照字典中key的顺序排序后再输出所有的值
for l in sorted(mlanguage.keys()):
    # print(l)
    print(mlanguage[l])




#定义一个字典
mlanguage = {"j":"java", "c":"c", "p":"python"}

#按照字典中value的顺序排序后再输出所有的值
for v in sorted(mlanguage.values()):
    print(v)