
#函数需要传递两个参数
def regUser (name, pwd) :
    print("name = {0}".format(name))
    print("pwd = {0}".format(pwd))


regUser("good", "123")

#函数需要传递两个参数
def regUser (name, pwd) :
    print("name = {0}".format(name))
    print("pwd = {0}".format(pwd))

#按照关键字传参的方式调用函数
regUser(pwd = "1234", name = "hehe")


#函数需要传递两个参数
#注意regUser使用了默认参数值
#再调用该函数时，可以不用指定pwd的值，而使用默认值
def regUser (name, pwd="000") :
    print("name = {0}".format(name))
    print("pwd = {0}".format(pwd))

#按照关键字传参的方式调用函数
regUser(name = "hehe")

#函数需要传递两个参数
#注意regUser使用了默认参数值
#再调用该函数时，可以不用指定nameName的值
#另外也不是所有的人都有nameName，所以把nameName放到最后
#让nameName成为可选的一个参数
def regUser (name, pwd, nakeName = "") :
    print("name = {0}".format(name))
    print("pwd = {0}".format(pwd))

#按照关键字传参的方式调用函数
regUser(pwd = "123", name = "hehe")
regUser(pwd = "123", name = "hehe", nakeName="sha")

#函数需要传递两个参数
#注意regUser使用了默认参数值
#再调用该函数时，可以不用指定nameName的值
#另外也不是所有的人都有nameName，所以把nameName放到最后
#让nameName成为可选的一个参数
#注意这个函数返回值，根据参数的不同返回不同数量的数据
#另外这个函数返回值不是普通数据而是一个字典
# def regUser (name, pwd, nakeName = "") :
#     if nakeName :
#         user = {"name":name, "pwd":pwd , "nameName":nakeName}
#     else :
#         user = {"name":name, "pwd":pwd}
#
#     return user
#
# #按照关键字传参的方式调用函数
# u = regUser("good", "4321", nakeName="gg")
# print(u)
#
#
# #定义一个函数，该函数能接收一个列表数据
# def getUserName(names) :
#     for n in names :
#         print(n)
#
# names = ["good", "luck", "to" ,"me"]
# getUserName(names)
#
#
# #定义一个函数，该函数能接收一个列表数据
# #注意再函数中对该列表参数进行了修改
# def getUserName(names) :
#     names.append("gun")
#
# #创建一个列表数据源
# names = ["good", "luck", "to" ,"me"]
# #调用函数，将列表数据源传递过去
# getUserName(names)
# #打印列表数据源
# #注意，该列表数据源是否发生改变
# print(names)


#定义一个函数，该函数能接收一个列表数据
#注意再函数中对该列表参数进行了修改
def getUserName(names):
    names.append("gun")

#创建一个列表数据源
names = ["good", "luck", "to" ,"me"]

#调用函数，将列表数据源传递过去
#注意再传递数据源时使用了特殊的用法
#该方法相当于对数据源进行复制
#最后注意打印数据源时，内容是否发生变化
getUserName(names[:])
#打印列表数据源
#注意，该列表数据源是否发生改变
print(names)


#定义一个函数，该函数能够接收任意多个参数
#注意参数前面有一个特殊符号：*
#注意该参数的数据类型，是元组
# def mulPara ( *params) :
#     print(type(params))
#     for p in params:
#         print(p)
#
# mulPara("good", "luck", "to", "me")

#定义一个函数，该函数能够接收任意多个参数
#注意参数前面有一个特殊符号：**
#注意该参数的数据类型，是字典
def mulPara (**params):
    print(type(params))
    for p in params.items():
        print(p)

#调用函数，使用字典的方式实现传参
mulPara(a="good", v="vv")
