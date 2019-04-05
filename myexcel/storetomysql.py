import pymysql

#服务器端的ip地址
serverIP = "localhost"

#数据库用户名
username = "root"

#数据库密码
password = ""

#数据库名
databaseName = "studentscore"

#在读取数据库中的图片时，使用的地址
mysqlPrePath = serverIP



if __name__ == '__main__':

    db = pymysql.connect(
        mysqlPrePath,  # 数据库对应的地址
        username,  # 数据库登录用户名
        password,  # 数据库登录密码
        databaseName  # 数据库名称
    )

    mcursor = db.cursor()

    mcursor.execute("insert into fiveTimesThery (sname) values('{sname}')".format(sname="hehehe"))

    db.commit()

    db.close()

