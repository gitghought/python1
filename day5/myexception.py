#打开一个不存在的文件
#使用只读方式打开
#注意这行代码会引发异常
#如果不使用异常处理，程序就此终止
# f = open("good.text","r")
#
# f.close()

#将可能发生异常的代码放到这段代码块中
try:
    # 打开一个不存在的文件
    # 使用只读方式打开
    # 注意这行代码会引发异常
    # 如果不使用异常处理，程序就此终止
    f = open("good.text", "r")

    f.close()

#此处捕获异常使用了所有异常的父类Exception
#一般来说应该先处理子类异常然后再处理父类异常
except Exception as e:
    print(e)

#如果try语句块中没有异常发生，
#   则会在执行完try中代码后执行else中的代码
else:
    print("excetion else")

#当处理完异常后就会执行这段代码区间中的程序
#无论是否发生异常，都会执行这段代码块中的代码
finally:
    print("finally")


#定义一个函数，如果参数是0，则手动抛出异常
def mfun(v) :
    if v == 0:
        raise Exception("good")


#捕获异常，并打印异常信息
try:
    mfun(0)
except Exception as e:
    print("excetp->{0}".format(e))
    pass

#查看异常处理后是否影响后续程序的运行
print("good")


class MyException (ZeroDivisionError) :
    print("myexception")
    pass


try:
    a = 10 / 0
except MyException as me :
    print("myexception -> {0}".format(me))
finally:
    print("finally")


print("enc")
