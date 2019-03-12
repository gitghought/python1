
#定义全局变量a1
a1 = 100

def mfun() :
    global a2 #声明a2为全局变量
    a2 = 10
    print("a1 = {0}".format(a1))

def mfun2():
    print("a2 = {0}".format(a2)) #在局部作用于内访问全局变量

mfun()
mfun2()
