
import xlwt
import xlrd

scoreExcelSrc = r"./xwx_ria_1702b.xls"

#按照表格的名称来获取指定的表格
scoreSheetName = u"成绩单"

#在成绩单表中，学生姓名的列值
nameColumnNumber = 6

degradeStudentCountColumnNumber = nameColumnNumber - 1

#返回指定学生名的末班次数
def getStudentDegradeCount(studentName) :
    pass

def getStudentName (line) :
    return line[nameColumnNumber]

def getAverageScore (scoreTheryAverage, scoreSkillAverage) :
    return (scoreSkillAverage + scoreTheryAverage) / 2

# 根据给定的成绩列表，求出平均成绩
# 本方法主要用于统计单科成绩的平均值
# 如求理论平均分或者技能平均分
"""
求出技能的平均成绩
"""
def getSkillAverageScore (scoreList) :
    sum = 0

    for s in scoreList :
        sum += s

    avgScore = sum / len(scoreList)

    print(avgScore)

    return avgScore


# 根据给定的成绩列表，求出平均成绩
# 本方法主要用于统计单科成绩的平均值
# 如求理论平均分或者技能平均分
"""
求出理论的平均成绩
"""
def getTheryAverageScore (scoreList) :
    sum = 0

    for s in scoreList :
        sum += s

    avgScore = sum / len(scoreList)

    print(avgScore)

    return avgScore

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

    rowValues = sheet0.row_values(13)
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

        scoreSkillAverage = getSkillAverageScore(scoreEveryDaySkill)

        avgScore = getAverageScore(scoreTheryAverage, scoreSkillAverage)
        print("avgScore = {avgScore}".format(avgScore = avgScore))

