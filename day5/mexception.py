
#自定义一个异常类
# 该自定义异常类是ValueError的子类
# 注意 类中没有任何有效代码，仅有一个站位用的pass
class MyException (ValueError) :
    pass

try:

    print("before raise exceptino ")

    #手动抛出异常
    # 注意 抛出的是自定义异常
    raise MyException

    print("after raise exceptino ")

#捕获自定义异常
except MyException as me:
    print("catch MyException")

#捕获自定义异常的父类
except ValueError as ve:
    print("catch ValueError")

#捕获所有异常的父类
except Exception as e:
    print("exception")
    print(e)

#如果没有异常发生则继续执行这段分支代码
else :
    print("try except else")

# 所有代码执行完成后，执行这段代码空间中的代码
finally:
    print("finally ")


#没有加任何异常处理
# print(5/0)



#使用try语句捕获异常
try:
    print(5/0)

#使用except处理异常
except ZeroDivisionError as e:
    print("zero Exception")

# print("输入两个数，计算除法")
# print("输入q退出")
#
# while True:
#     print("\t")
#     fnum = input("First number:")
#     if fnum == "q":
#         break
#
#     snum = input("Second number:")
#     if snum == "q":
#         break
#
#     res = int(fnum) / int(snum)
#
#     print("result = {0}".format(res))


# print("输入两个数，计算除法")
# print("输入q退出")
#
# while True:
#     print("\t")
#     fnum = input("First number:")
#     if fnum == "q":
#         break
#
#     snum = input("Second number:")
#     if snum == "q":
#         break
#
#     #捕获异常，如果发生则进入异常的分支代码块
#     try:
#         res = int(fnum) / int(snum)
#     #异常分支代码块
#     #在代码块中处理异常
#     except ZeroDivisionError as e:
#         print("division error")
#     #如果没有发生异常，则执行这段代码
#     else :
#         print("result = {0}".format(res))
#     finally :
#         print("在这里处理一些收尾工作，如果有")

print("输入两个数，计算除法")
print("输入q退出")

while True:
    print("\t")
    fnum = input("First number:")
    if fnum == "q":
        break

    snum = input("Second number:")
    if snum == "q":
        break

    #捕获异常，如果发生则进入异常的分支代码块
    try:
        res = int(fnum) / int(snum)
    #异常分支代码块
    #在代码块中处理异常
    #注意此处的代码中只有一个pass
    # 表示什么都不做
    except ZeroDivisionError as e:
        pass

    #如果没有发生异常，则执行这段代码
    else :
        print("result = {0}".format(res))
    finally :
        # print("在这里处理一些收尾工作，如果有")
        pass
