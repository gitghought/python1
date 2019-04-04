
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

def getTheryAverageScore (scoreList) :
    pass

# 从每天的成绩中筛选出每天的技能成绩
def getEveryDaySkillScore (scoreEveryDay) :
    scoreEveryDaySkill = scoreEveryDay[1::2]
    print(scoreEveryDaySkill)


# 从每天的成绩中筛选出每天的理论成绩
def getEveryDayTheryScore (scoreEveryDay) :
    scoreEveryDayThery = scoreEveryDay[::2]
    print(scoreEveryDayThery)

#获取完一行数据后，使用切片，将学生每天的成绩取出来
#   数据包含日考、周考和月考
def getEveryDayScoreFromLine(line) :
    scoreEveryDay = line[nameColumnNumber + 1:len(line) - 1]
    # print(len(scoreEveryDay))

    return scoreEveryDay

if __name__ == '__main__':
    workBook = xlrd.open_workbook(scoreExcelSrc)

    sheet0 = workBook.sheet_by_name(scoreSheetName)

    rowValues = sheet0.row_values(9)
    # print("rowValues = {rowValues}".format(rowValues = rowValues))
    # print(type(rowValues))

    scoreEveryDay = getEveryDayScoreFromLine(rowValues)

    getEveryDayTheryScore(scoreEveryDay)

    getEveryDaySkillScore(scoreEveryDay)
