
# #创建一个用户列表
# #这些用户都是尚未注册的
# unUser = ["user1", "user2", "user3"]
#
# #准备一个已经注册的用户列表
# #初始为空
# conUsers = []
#
# #通过input输入用户名
# #来选择用户名，并保存到已确认用户列表中
# conUser = input("哪个用户已经注册过了？")
#
# #设置索引的起始下标
# mpos = 0
# #通过循环遍历未注册列表
# #如果找到对应用户名，则保存到已注册列表中
# while True:
#     #判断退出循环的条件
#     if conUser != unUser[mpos] :
#         mpos += 1
#
#         if unUser.__len__() <= mpos :
#             break
#
#     #判断找到用户后的程序动作
#     if conUser == unUser[mpos]:
#         conUsers.append(unUser.pop(mpos))
#         break
#
# print(conUsers)


#创建一个用户列表
#这些用户都是尚未注册的
unUser = ["user1", "user2", "user3"]

#准备一个已经注册的用户列表
#初始为空
conUsers = []

#通过input输入用户名
#来选择用户名，并保存到已确认用户列表中
conUser = input("哪个用户已经注册过了？")

#设置索引的起始下标
mpos = 0
#通过循环遍历未注册列表
#如果找到对应用户名，则保存到已注册列表中
while conUser in unUser:
        conUsers.append(unUser.pop(unUser.index(conUser)))

print(conUsers)
