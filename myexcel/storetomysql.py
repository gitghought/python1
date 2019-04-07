import pymysql
import json

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

keyFiveTimesClass = "sclass"

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
    keySname = "sname"
    keySkillAvgList = [ "fiveDaySkillAvg", "tenDaySkillAvg", "fiftenDaySkillAvg", "monthSkillAvg" ]
    keyTheryAvgList = [ "fiveDayTheryAvg", "tenDayTheryAvg", "fiftenDayTheryAvg", "monthTheryAvg" ]
    keyEveryDayTheryList = [
        "day0",
        "day1",
        "day2",
        "day3",
        "day4",
        "day5",
        "day6",
        "day7",
        "day8",
        "day9",
        "day10",
        "day11",
        "day12",
        "day13",
        "day14",
        "day15",
        "day16",
        "day17",
        "day18",
        "day19",
        "day20",
        "day21"
    ]

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

    # 用于将班级信息组成一个元组
    def getClassTuple(sclass):
        return ("sclass", sclass)

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
                fiftenDaySkillAvg=dict[keyFiveTimesSkillFifteenDaySkillAvg],
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
        this.cursor = this.getCursor()
        #执行向数据库插入数据的操作
        this.cursor.execute("insert into "
                            "fiveTimesThery ("
                            "sname,"
                            "fiveDayTheryAvg,"
                            "tenDayTheryAvg,"
                            "fiftenDayTheryAvg,"
                            "monthTheryAvg,"
                            "sclass"
                            ") "
                            "values("
                            "'{sname}',"
                            "'{fiveDayTheryAvg}',"
                            "'{tenDayTheryAvg}',"
                            "'{fiftenDayTheryAvg}',"
                            "'{monthTheryAvg}',"
                            "'{sclass}'"
                            ")".format(
            sname=dict[keyFiveTimesTherySname],
            fiveDayTheryAvg=dict[keyFiveTimesTheryFiveDayTheryAvg],
            tenDayTheryAvg=dict[keyFiveTimesTheryTenDayTheryAvg],
            fiftenDayTheryAvg=dict[keyFiveTimesTheryFiftenDayTheryAvg],
            monthTheryAvg=dict[keyFiveTimesTheryMonthTheryAvg],
            sclass=dict[keyFiveTimesClass]
        ))

        this.db.commit()

        # 将封装好数据的字典添加到数据库种
        # 字典种必须封装表中需要的所有数据

    def insertIntoEveryDayTheryDict(this, dict):
        # 执行向数据库插入数据的操作
        this.cursor = this.getCursor()

        # 执行向数据库插入数据的操作
        this.cursor.execute("insert into "
                            "everydaythery ("
                            "sname,"
                            "day1 ,"
                            "day2 ,"
                            "day3 ,"
                            "day4 ,"
                            "day5 ,"
                            "day6 ,"
                            "day7 ,"
                            "day8 ,"
                            "day9 ,"
                            "day10,"
                            "day11,"
                            "day12,"
                            "day13,"
                            "day14,"
                            "day15,"
                            "day16,"
                            "day17,"
                            "day18,"
                            "day19,"
                            "day20,"
                            "day21"
                            ") "
                            "values("
                            "'{sname}',"
                            "'{day1}',"
                            "'{day2}',"
                            "'{day3}',"
                            "'{day4}',"
                            "'{day5}',"
                            "'{day6}',"
                            "'{day7}',"
                            "'{day8}',"
                            "'{day9}',"
                            "'{day10}',"
                            "'{day11}',"
                            "'{day12}',"
                            "'{day13}',"
                            "'{day14}',"
                            "'{day15}',"
                            "'{day16}',"
                            "'{day17}',"
                            "'{day18}',"
                            "'{day19}',"
                            "'{day20}',"
                            "'{day21}'"
                            ")".format(
            sname=dict[this.keySname],
            day1 =dict[this.keyEveryDayTheryList[1]],
            day2 =dict[this.keyEveryDayTheryList[2]],
            day3 =dict[this.keyEveryDayTheryList[3]],
            day4 =dict[this.keyEveryDayTheryList[4]],
            day5 =dict[this.keyEveryDayTheryList[5]],
            day6 =dict[this.keyEveryDayTheryList[6]],
            day7 =dict[this.keyEveryDayTheryList[7]],
            day8 =dict[this.keyEveryDayTheryList[8]],
            day9 =dict[this.keyEveryDayTheryList[9]],
            day10=dict[this.keyEveryDayTheryList[10]],
            day11=dict[this.keyEveryDayTheryList[11]],
            day12=dict[this.keyEveryDayTheryList[12]],
            day13=dict[this.keyEveryDayTheryList[13]],
            day14=dict[this.keyEveryDayTheryList[14]],
            day15=dict[this.keyEveryDayTheryList[15]],
            day16=dict[this.keyEveryDayTheryList[16]],
            day17=dict[this.keyEveryDayTheryList[17]],
            day18=dict[this.keyEveryDayTheryList[18]],
            day19=dict[this.keyEveryDayTheryList[19]],
            day20=dict[this.keyEveryDayTheryList[20]],
            day21=dict[this.keyEveryDayTheryList[21]],
        ))

        this.db.commit()

    # 当执行完数据库查询操作后，
    # 将查询的数据取出保存到字典
    # 再将每个字典添加到一个列表
    # 最后将列表返回
    def __getValuesFromCursor(this):

        slist = []
        sdict = {}

        rows = this.cursor.fetchall()

        for row in rows :

            avglist = []
            #获取四次平均成绩，每组平均成绩存放到一个元组中
            for pos in range(4) :
                # print(row[2 + pos].rjust(20, " "), end="  ")
                mtuple = (this.keyTheryAvgList[pos], row[2+pos])
                avglist.append(mtuple)

            #将四次均分做成一个字典
            avgDict = dict(avglist)

            # 将学生姓名与他四次的均分做成一个新的字典
            # 是嵌套字典
            sdict = {row[1]:avgDict}
            # print(sdict)

            slist.append(sdict)

        return slist

    # 从数据库中检索数据
    # orderby指定排序的规则
    # 该函数返回的是一个由字段做元素的列表
    def selectFromFiveTimesThery(this, orderby):
        this.getCursor()
        this.cursor.execute(
            "SELECT * FROM "
            "`fiveTimesThery` "
            "order by {orderby} "
            "desc limit 0,34".format(orderby=orderby)
        )

        slist= this.__getValuesFromCursor()

        this.db.commit()

        # print(slist)

        return slist


    #执行关闭数据库的操作
    # 在完成一个数据库操作后就执行这个函数
    def disConnect(this):
        this.db.close()

if __name__ == '__main__':

    dictScore = {
        "sname":"hehehehe",
        "day1":"day1",
        "day2":"day2",
        "day3":"day3",
        "day4":"day4",
        "day5":"day5",
        "day6":"day6",
        "day7":"day7",
        "day8":"day8",
        "day9":"day9",
        "day10":"day10",
        "day11":"day11",
        "day12":"day12",
        "day13":"day13",
        "day14":"day14",
        "day15":"day15",
        "day16":"day16",
        "day17":"day17",
        "day18":"day18",
        "day19":"day19",
        "day20":"day20",
        "day21":"day21"
    }


    """
   
    以下是数据库使用的步骤 
        1、创建数据库对象
        2、添加数据库到数据库
        3、关闭数据库连接
    
    """
    #创建数据库对象
    mstm = ScoreToMySQL()

    # # 将准备的字典数据添加到数据库
    mstm.insertIntoEveryDayTheryDict(dictScore)

    # mstm.selectFromFiveTimesThery(mstm.keyTheryAvgList[3])

    # 关闭本次数据库连接
    mstm.disConnect()


