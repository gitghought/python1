import os


class MyInclude () :
    #存储学生成绩的文件夹名称
    studentScoreExcelFolder = r".\studentscoreexcel"


    #存储学生成绩分析后的文件夹名称
    studentScoreAnalizeExcelFolder = r"studentscoreanalize"

    # 学校成绩单文件名，不包含
    # scoreExcelPrefix = "python1_gh"
    scoreExcelPrefix = "java6"

    scoreExcelSrc = "{mclass}.xls".format(mclass=scoreExcelPrefix)
    scoreExcelXSrc = "{mclass}.xlsx".format(mclass=scoreExcelPrefix)

    scoreExcelAbsPath = os.path.abspath(os.path.join(studentScoreExcelFolder, scoreExcelSrc))
    scoreExcelXAbsPath = os.path.abspath(os.path.join(studentScoreExcelFolder, scoreExcelXSrc))

    # 按照表格的名称来获取指定的表格
    scoreSheetName = u"成绩单"