import xlrd
from myexcel import storetomysql

from myexcel.MyInclude import MyInclude

class PickStudent ():

    # 在一个班级里，最多允许有60人
    studentLimitation = 60

    # 在成绩单一栏中，学生成绩开始的行号
    studentScoreStartPos = 8

    # 在成绩单表中，学生姓名的列值
    nameColumnNumber = 6

    # 在成绩单一栏中，学生成绩结束的行号
    studentScoreStopPos = studentScoreStartPos + studentLimitation

    # 末班学生次数统计数的列号
    degradeStudentCountColumnNumber = nameColumnNumber - 1

    def __init__(this, path):
        this.path = path

    #根据文件路径打开Excel表格文件
    def myXlsOpen(this):
        this.workbook = xlrd.open_workbook(this.path)
        return this.workbook

    #根据文件路径打开Excel表格文件
    # 根据指定的路径打开excel表格
    def myXlsOpenWithPath(this, path):
        this.workbook = xlrd.open_workbook(path)
        return this.workbook

    #打开Excel表格文件中的指定表格
    # 返回指定表格对象
    def getSheetByName(this):
        this.sheet = this.workbook.sheet_by_name(MyInclude.scoreSheetName)
        return this.sheet

    # 从已经打开的表格种获取指定行的所有列的值
    # 所有的列的值都存储在一个列表种
    def getRowValues(this, rowNumber):
        this.rowValueList = this.sheet.row_values(rowNumber)

        return this.rowValueList

    # 判断当前读取的一行是否是空行或者是无效行
    def isNoneLine(this, line):
        if line[this.nameColumnNumber] == "":
            return True

    # 从完整的一行中读取学生的姓名
    # 返回与数据库对应的元祖
    # 键：sname
    # 值：学生姓名
    def getStudentNameTuple(this):
        line = this.rowValueList
        return ("sname", line[this.nameColumnNumber])

    # 返回指定学生名的末班次数
    def getStudentDegradeCountTuple(this):
        return ("degradeCount", this.rowValueList[this.degradeStudentCountColumnNumber])

    # 根据指定成绩单，求指定天数的平均成绩
    # 既可以求理论平均成绩，又可以求技能平均成绩
    # 该方法时私有方法，不被外界调用
    def __getAverageScoreByDays(this, scoreList, nday):
        sum = 0

        try:
            for s in scoreList[:nday]:
                if s == "请假" or s == "作弊" or s == "旷考" or s == "休学":
                    sum += 0
                else:
                    sum += s
        except TypeError as e:
            pass

        print("sum = " + str(sum))

        return sum / nday

    # 获取完一行数据后，使用切片，将学生每天的成绩取出来
    #   数据包含日考、周考和月考
    def getEveryDayScoreFromLine(this):
        line = this.rowValueList
        this.scoreEveryDay = line[this.nameColumnNumber + 1:len(line) - 1]

        return this.scoreEveryDay

    # 从每天的成绩中筛选出每天的理论成绩
    def getEveryDayTheryScore(this):
        this.getEveryDayScoreFromLine()
        this.scoreEveryDayThery = this.scoreEveryDay[::2]
        # print(scoreEveryDayThery)

        return this.scoreEveryDayThery

    # 从每天的成绩中筛选出每天的技能成绩
    def getEveryDaySkillScore(this):
        this.getEveryDayScoreFromLine()
        this.scoreEveryDaySkill = this.scoreEveryDay[1::2]

        return this.scoreEveryDaySkill

    # 能够求理论5日的均分
    def getFiveDayTheryAverageScore(this):
        this.getEveryDayTheryScore()
        fiveDayTheryAverageScore = this.__getAverageScoreByDays(this.scoreEveryDayThery, 5)

        return fiveDayTheryAverageScore

    # 能够求理论5日的均分
    # 返回元组数据
    def getFiveDayTheryAverageScoreTuple(this):
        return (storetomysql.keyFiveTimesTheryFiveDayTheryAvg, this.getFiveDayTheryAverageScore())

    # 能够求技能5日的均分
    def getFiveDaySkillAverageScore(this):
        this.getEveryDaySkillScore()
        print(this.scoreEveryDaySkill)
        return this.__getAverageScoreByDays(this.scoreEveryDaySkill, 5)

    # 能够求技能5日的均分
    def getFiveDaySkillAverageScoreTuple(this):
        return (storetomysql.keyFiveTimesSkillFiveDaySkillAvg, this.getFiveDaySkillAverageScore())

    # 能够求理论10日的均分
    def getTenDayTheryAverageScore(this):
        this.getEveryDayTheryScore()
        return this.__getAverageScoreByDays(this.scoreEveryDayThery, 10)
        # 能够求理论10日的均分

    def getTenDayTheryAverageScoreTuple(this):
        return (storetomysql.keyFiveTimesTheryTenDayTheryAvg, this.getTenDayTheryAverageScore())

    # 能够求技能10日的均分
    def getTenDaySkillAverageScore(this):
        this.getEveryDaySkillScore()
        return this.__getAverageScoreByDays(this.scoreEveryDaySkill, 10)

    # 能够求技能10日的均分
    def getTenDaySkillAverageScoreTuple(this):
        return (storetomysql.keyFiveTimesSkillTenDaySkillAvg, this.getTenDaySkillAverageScore())

    # 能够求理论15日的均分
    def getFifteenDayTheryAverageScore(this):
        this.getEveryDayTheryScore()
        return this.__getAverageScoreByDays(this.scoreEveryDayThery, 15)

    # 能够求理论15日的均分
    def getFifteenDayTheryAverageScoreTuple(this):
        return (storetomysql.keyFiveTimesTheryFiftenDayTheryAvg, this.getFifteenDayTheryAverageScore())

    # 能够求技能15日的均分
    def getFifteenDaySkillAverageScore(this):
        this.getEveryDaySkillScore()
        return this.__getAverageScoreByDays(this.scoreEveryDaySkill, 15)

    # 能够求技能15日的均分
    def getFifteenDaySkillAverageScoreTuple(this):
        return (storetomysql.keyFiveTimesSkillFifteenDaySkillAvg, this.getFifteenDaySkillAverageScore())

    # 能够求理论月的均分
    def getMonthTheryAverageScore(this):
        this.getEveryDayTheryScore()
        monthTheryAvgScore = this.__getAverageScoreByDays( \
            this.scoreEveryDayThery, len(this.scoreEveryDayThery))

        return monthTheryAvgScore

    # 能够求理论月的均分
    def getMonthTheryAverageScoreTuple(this):
        return (storetomysql.keyFiveTimesTheryMonthTheryAvg, this.getMonthTheryAverageScore())

    # 能够求技能月的均分
    def getMonthSkillAverageScore(this):
        this.getEveryDaySkillScore()
        monthSkillAvgScore = this.__getAverageScoreByDays( \
            this.scoreEveryDaySkill, len(this.scoreEveryDaySkill))
        return monthSkillAvgScore

    def getMonthSkillAverageScoreTuple(this):
        return (storetomysql.keyFiveTimesSkillMonthSkillAvg, this.getMonthSkillAverageScore())

    # 求理论和技能的满月平均成绩
    def getAverageScore(this):
        return (this.getMonthTheryAverageScore() +  \
        this.getMonthSkillAverageScore()) / 2
        # return (scoreSkillAverage + scoreTheryAverage) / 2
