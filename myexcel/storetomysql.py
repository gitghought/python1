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

keyFiveTimesTherySname = "sname"
keyFiveTimesTheryFiveDayTheryAvg= "fiveDayTheryAvg"
keyFiveTimesTheryTenDayTheryAvg= "tenDayTheryAvg"
keyFiveTimesTheryFiftenDayTheryAvg= "fiftenDayTheryAvg"
keyFiveTimesTheryMonthTheryAvg= "monthTheryAvg"

keyFiveTimesSkillSname = "sname"
keyFiveTimesSkillFiveDaySkillAvg= "fiveDaySkillAvg"
keyFiveTimesSkillTenDaySkillAvg= "tenDaySkillAvg"
keyFiveTimesSkillFifteenDaySkillAvg= "fiftenDaySkillAvg"
keyFiveTimesSkillMonthSkillAvg= "monthSkillAvg"

class ScoreToMySQL :

    def myConnect(this):

        this.db = pymysql.connect(
            mysqlPrePath,  # 数据库对应的地址
            username,  # 数据库登录用户名
            password,  # 数据库登录密码
            databaseName  # 数据库名称
        )

        return this.db

    #返回一个游标
    def getCursor(this):

        #如果在此处发生异常，说明当前对象还没有调用myConnect方法
        try:

            this.cursor = this.db.cursor()

        except AttributeError as e :

            this.myConnect()

        else :

            pass

        finally :

            this.cursor = this.db.cursor()

            return this.cursor


    #将封装好数据的字典添加到数据库种
    # 字典种必须封装表中需要的所有数据
    def insertIntoFiveTimesSkillDict(this, dict):
        try :
            #执行向数据库插入数据的操作
            this.cursor.execute("insert into "
                                "fiveTimesSkill ("
                                "sname,"
                                "fiveDaySkillAvg,"
                                "tenDaySkillAvg,"
                                "fiftenDaySkillAvg,"
                                "monthSkillAvg"
                                ") "
                                "values("
                                "'{sname}',"
                                "'{fiveDaySkillAvg}',"
                                "'{tenDaySkillAvg}',"
                                "'{fiftenDaySkillAvg}',"
                                "'{monthSkillAvg}'"
                                ")".format(
                sname=dict[keyFiveTimesSkillSname],
                fiveDaySkillAvg=dict[keyFiveTimesSkillFiveDaySkillAvg],
                tenDaySkillAvg=dict[keyFiveTimesSkillTenDaySkillAvg],
                fiftenDaySkillAvg=dict[keyFiveTimesSkillFiftenDaySkillAvg],
                monthSkillAvg=dict[keyFiveTimesSkillMonthSkillAvg]
            ))
        except AttributeError as e:
            this.cursor = this.getCursor()

        else :
            pass
            this.db.commit()
        finally:

            # 执行向数据库插入数据的操作
            this.cursor.execute("insert into "
                                "fiveTimesSkill ("
                                "sname,"
                                "fiveDaySkillAvg,"
                                "tenDaySkillAvg,"
                                "fiftenDaySkillAvg,"
                                "monthSkillAvg"
                                ") "
                                "values("
                                "'{sname}',"
                                "'{fiveDaySkillAvg}',"
                                "'{tenDaySkillAvg}',"
                                "'{fiftenDaySkillAvg}',"
                                "'{monthSkillAvg}'"
                                ")".format(
                sname=dict[keyFiveTimesSkillSname],
                fiveDaySkillAvg=dict[keyFiveTimesSkillFiveDaySkillAvg],
                tenDaySkillAvg=dict[keyFiveTimesSkillTenDaySkillAvg],
                fiftenDaySkillAvg=dict[keyFiveTimesSkillFifteenDaySkillAvg],
                monthSkillAvg=dict[keyFiveTimesSkillMonthSkillAvg]
            ))

            this.db.commit()

    #将封装好数据的字典添加到数据库种
    # 字典种必须封装表中需要的所有数据
    def insertIntoFiveTimesTheryDict(this, dict):
        try :
            #执行向数据库插入数据的操作
            this.cursor.execute("insert into "
                                "fiveTimesThery ("
                                "sname,"
                                "fiveDayTheryAvg,"
                                "tenDayTheryAvg,"
                                "fiftenDayTheryAvg,"
                                "monthTheryAvg"
                                ") "
                                "values("
                                "'{sname}',"
                                "'{fiveDayTheryAvg}',"
                                "'{tenDayTheryAvg}',"
                                "'{fiftenDayTheryAvg}',"
                                "'{monthTheryAvg}'"
                                ")".format(
                sname=dict[keyFiveTimesTherySname],
                fiveDayTheryAvg=dict[keyFiveTimesTheryFiveDayTheryAvg],
                tenDayTheryAvg=dict[keyFiveTimesTheryTenDayTheryAvg],
                fiftenDayTheryAvg=dict[keyFiveTimesTheryFiftenDayTheryAvg],
                monthTheryAvg=dict[keyFiveTimesTheryMonthTheryAvg]
            ))
        except AttributeError as e:
            this.cursor = this.getCursor()

        else :
            pass
            this.db.commit()
        finally:

            # 执行向数据库插入数据的操作
            this.cursor.execute("insert into "
                                "fiveTimesThery ("
                                "sname,"
                                "fiveDayTheryAvg,"
                                "tenDayTheryAvg,"
                                "fiftenDayTheryAvg,"
                                "monthTheryAvg"
                                ") "
                                "values("
                                "'{sname}',"
                                "'{fiveDayTheryAvg}',"
                                "'{tenDayTheryAvg}',"
                                "'{fiftenDayTheryAvg}',"
                                "'{monthTheryAvg}'"
                                ")".format(
                sname=dict[keyFiveTimesTherySname],
                fiveDayTheryAvg=dict[keyFiveTimesTheryFiveDayTheryAvg],
                tenDayTheryAvg=dict[keyFiveTimesTheryTenDayTheryAvg],
                fiftenDayTheryAvg=dict[keyFiveTimesTheryFiftenDayTheryAvg],
                monthTheryAvg=dict[keyFiveTimesTheryMonthTheryAvg]
            ))

            this.db.commit()

    #执行关闭数据库的操作
    # 在完成一个数据库操作后就执行这个函数
    def disConnect(this):
        this.db.close()

if __name__ == '__main__':

    dictScore = {
        "sname":"hehehehe",
        "fiveDayTheryAvg":"12",
        "tenDayTheryAvg":"12",
        "fiftenDayTheryAvg":"12",
        "monthTheryAvg":"12"
    }


    """
   
    以下是数据库使用的步骤 
        1、创建数据库对象
        2、添加数据库到数据库
        3、关闭数据库连接
    
    """
    #创建数据库对象
    mstm = ScoreToMySQL()

    # 将准备的字典数据添加到数据库
    mstm.insertIntoFiveTimesTheryDict(dictScore)

    # 关闭本次数据库连接
    mstm.disConnect()


