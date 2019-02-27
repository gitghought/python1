
#在当前文件夹下以可写方式打开一个文件
#注意如果该文件不存在则创建一个新的文件
#第一个参数前面使用了一个r字符，表示路径不需要进行转义
f = open(r"./test.txt", "w")

#关闭打开的文件
f.close()


#在当前文件夹下以可写方式打开一个文件
#注意如果该文件不存在则创建一个新的文件
#第一个参数前面使用了一个r字符，表示路径不需要进行转义
f = open(r"./test.txt", "w")

len = f.write("good good study , day day up\n")
len = f.write("good good study , day day up\n")
len = f.write("good good study , day day up\n")
len = f.write("good good study , day day up\n")
len = f.write("good good study , day day up\n")
print(len)

#关闭打开的文件
f.close()

#在当前文件夹下以只读方式打开一个文件
#注意如果该文件不存，则会抛出异常
#可以使用异常处理机制来解决这个问题
#第一个参数前面使用了一个r字符，表示路径不需要进行转义
f = open(r"./test.txt", "r")

#从打开的文件中读取1024个字节
fbuf = f.read(1024)
print("fbuf = {0}".format(fbuf))

#关闭打开的文件
f.close()


#在当前文件夹下以只读方式打开一个文件
#注意如果该文件不存，则会抛出异常
#可以使用异常处理机制来解决这个问题
#第一个参数前面使用了一个r字符，表示路径不需要进行转义
f = open(r"./test.txt", "r")

#从打开的文件中读取该文件的一行
#一般是逐行读取
#可以使用for循环读取文件中所有的行
fbuf = f.readline()

print("fbuf = {0}".format(fbuf))

#关闭打开的文件
f.close()


#在当前文件夹下以只读方式打开一个文件
#注意如果该文件不存，则会抛出异常
#可以使用异常处理机制来解决这个问题
#第一个参数前面使用了一个r字符，表示路径不需要进行转义
f = open(r"./test.txt", "r")

#从打开的文件中读取该文件的一行
#一般是逐行读取
#可以使用for或者while循环读取文件中所有的行
while  True :
    fbuf = f.readline()
    if fbuf.__len__() == 0:
        break
    print("line = {0}".format(fbuf))

#关闭打开的文件
f.close()


#在当前文件夹下以只读方式打开一个文件
#注意如果该文件不存，则会抛出异常
#可以使用异常处理机制来解决这个问题
#第一个参数前面使用了一个r字符，表示路径不需要进行转义
f = open(r"./test.txt", "r")

#从打开的文件中读取该文件的一行
#一般是逐行读取
#可以使用for或者while循环读取文件中所有的行
#使用readlines将文件中所有行都读取到fbufs中
fbufs = f.readlines()

#使用for遍历读取出的所有行
for l in fbufs :
    print(l)

#关闭打开的文件
f.close()


#在当前文件夹下以只读方式打开一个文件
#注意如果该文件不存，则会抛出异常
#可以使用异常处理机制来解决这个问题
#第一个参数前面使用了一个r字符，表示路径不需要进行转义
f = open(r"./test.txt", "r")

#从打开的文件中读取该文件的一行
#一般是逐行读取
#可以使用for或者while循环读取文件中所有的行
while  True :
    fbuf = f.readline()
    if fbuf.__len__() == 0:
        break
    print("line = {0}".format(fbuf))

    #使用tell获取当前位置并打印
    fpos = f.tell()
    print("fpos = {0}".format(fpos))

#关闭打开的文件
f.close()

#在当前文件夹下以只读方式打开一个文件
#注意如果该文件不存，则会抛出异常
#可以使用异常处理机制来解决这个问题
#第一个参数前面使用了一个r字符，表示路径不需要进行转义
f = open(r"./a.png", "rb")
fdst = open(r"b.png", "wb")

#从打开的文件中读取该文件的一行
#一般是逐行读取
#可以使用for或者while循环读取文件中所有的行
fbuf = f.read()
fdst.write(fbuf)

#关闭打开的文件
fdst.close()
f.close()
