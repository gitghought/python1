
#定义一个修饰器
#注意该修饰器有一个参数
#该参数是被修饰的函数
#也就是函数的参数是一个函数
def mydef (f) :

    #定义内部函数
    #先在被修饰函数前面执行一段代码
    #然后将被修饰的函数执行后的结果返回
    def ven (*a, **b):
        print("good")
        return f()

    #返回内部函数
    return ven

#使用@符号加上修饰器函数名来修饰被修饰的函数
@mydef
def myhel () :
    print("hello")

#调用被修饰的函数
myhel ()