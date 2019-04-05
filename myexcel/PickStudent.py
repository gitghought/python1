import xlrd

class PickStudent ():
    # 按照表格的名称来获取指定的表格
    scoreSheetName = u"成绩单"

    # 在一个班级里，最多允许有60人
    studentLimitation = 60

    # 在成绩单一栏中，学生成绩开始的行号
    studentScoreStartPos = 8

    # 在成绩单表中，学生姓名的列值
    nameColumnNumber = 6

    # 在成绩单一栏中，学生成绩结束的行号
    studentScoreStopPos = studentScoreStartPos + studentLimitation


    def __init__(self):
        pass

    #根据文件路径打开Excel表格文件
    def myXlsOpen(this, path):
        this.workbook = xlrd.open_workbook(path)
        return this.workbook

    #打开Excel表格文件中的指定表格
    # 返回指定表格对象
    def getSheetByName(this, sheetName):
        this.sheet = this.workbook.sheet_by_name(sheetName)
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
    def getStudentNameTuple(this, line):
        return ("sname", line[this.nameColumnNumber])

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

        return sum / nday

    # 获取完一行数据后，使用切片，将学生每天的成绩取出来
    #   数据包含日考、周考和月考
    def getEveryDayScoreFromLine(this, line):
        scoreEveryDay = line[this.nameColumnNumber + 1:len(line) - 1]

        return scoreEveryDay