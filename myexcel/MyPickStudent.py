
import xlwt
import xlrd

scoreExcelSrc = r"./xwx_ria_1702b.xls"

#按照表格的名称来获取指定的表格
scoreSheetName = u"成绩单"

#在一个班级里，最多允许有60人
studentLimitation = 60

#在成绩单一栏中，学生成绩开始的行号
studentScoreStartPos = 8

#在成绩单一栏中，学生成绩结束的行号
studentScoreStopPos = studentScoreStartPos + studentLimitation

#在成绩单表中，学生姓名的列值
nameColumnNumber = 6

#末班学生次数统计数的列号
degradeStudentCountColumnNumber = nameColumnNumber - 1

#返回指定学生名的末班次数
def getStudentDegradeCount(studentName) :
    pass

#从完整的一行中读取学生的姓名
def getStudentName (line) :
    return line[nameColumnNumber]

def getAverageScore (scoreTheryAverage, scoreSkillAverage) :
    return (scoreSkillAverage + scoreTheryAverage) / 2

def getAverageScoreByDays(scoreList, nday) :
    sum = 0

    for s in scoreList[:nday] :
        sum += s

    return sum / nday


# 根据给定的成绩列表，求出平均成绩
# 本方法主要用于统计单科成绩的平均值
# 如求理论平均分或者技能平均分
"""
求出技能的平均成绩
一个教学周期的技能平均成绩
"""
def getSkillAverageScore (scoreList) :
    # sum = 0
    #
    # for s in scoreList :
    #     sum += s
    #
    # avgScore = sum / len(scoreList)
    #
    # # print(avgScore)

    return getAverageScoreByDays(scoreList, len(scoreList))


# 根据给定的成绩列表，求出平均成绩
# 本方法主要用于统计单科成绩的平均值
# 如求理论平均分或者技能平均分
"""
求出理论的平均成绩
一个教学周期的理论平均成绩
"""
def getTheryAverageScore (scoreList) :
    # sum = 0
    #
    # for s in scoreList :
    #     sum += s
    #
    # avgScore = sum / len(scoreList)
    #
    # # print(avgScore)
    return getAverageScoreByDays(scoreList, len(scoreList))

# 从每天的成绩中筛选出每天的技能成绩
def getEveryDaySkillScore (scoreEveryDay) :
    scoreEveryDaySkill = scoreEveryDay[1::2]
    # print(scoreEveryDaySkill)

    return scoreEveryDaySkill


# 从每天的成绩中筛选出每天的理论成绩
def getEveryDayTheryScore (scoreEveryDay) :
    scoreEveryDayThery = scoreEveryDay[::2]
    # print(scoreEveryDayThery)

    return scoreEveryDayThery

#获取完一行数据后，使用切片，将学生每天的成绩取出来
#   数据包含日考、周考和月考
def getEveryDayScoreFromLine(line) :
    scoreEveryDay = line[nameColumnNumber + 1:len(line) - 1]
    # print(len(scoreEveryDay))

    return scoreEveryDay

# 判断当前读取的一行是否是空行或者是无效行
def isNoneLine(line) :
    if line[nameColumnNumber] == "" :
        return True

if __name__ == '__main__':
    workBook = xlrd.open_workbook(scoreExcelSrc)

    sheet0 = workBook.sheet_by_name(scoreSheetName)

    rowValues = sheet0.row_values(8)
    if isNoneLine(rowValues) :
        pass
    else :
        print("rowValues = {rowValues}".format(rowValues = rowValues))
        # print(type(rowValues))

        studentName = getStudentName(rowValues)
        print("studentName = {studentName}".format(studentName = studentName))

        scoreEveryDay = getEveryDayScoreFromLine(rowValues)

        scoreEveryDayThery = getEveryDayTheryScore(scoreEveryDay)
        scoreEveryDaySkill = getEveryDaySkillScore(scoreEveryDay)

        scoreTheryAverage = getTheryAverageScore(scoreEveryDayThery)
        print("scoreTheryAverage = " + str(scoreTheryAverage))

        scoreSkillAverage = getSkillAverageScore(scoreEveryDaySkill)
        print("scoreSkillAverage = " + str(scoreSkillAverage))

        avgScore = getAverageScore(scoreTheryAverage, scoreSkillAverage)
        print("avgScore = {avgScore}".format(avgScore = avgScore))

