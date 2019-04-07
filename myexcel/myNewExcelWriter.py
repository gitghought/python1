# from myexcel.PickStudent import PickStudent

from myexcel.storetomysql import  ScoreToMySQL

from myexcel.MyInclude import MyInclude

import xlsxwriter


class DictToExcel():
    fileName = "avg{filename}.xls".format(filename=MyInclude.scoreExcelPrefix)
    studentCount = 34

    def __init__(this):
        this.workbook = xlsxwriter.Workbook(filename=this.fileName)

    def createNewSheetByName(this, name):
        this.worksheet = this.workbook.add_worksheet(name)

    def createNewSheet(this):
        this.worksheet = this.workbook.add_sheet(mstm.keyTheryAvgList[0])

    def WriteTitleToSheet(this):
        pass

    """

        {'宋成安': 
            {
                'fiveDayTheryAvg': '54.4', 
                'tenDayTheryAvg': '71.3', 
                'fiftenDayTheryAvg': '75.46666666666667', 
                'monthTheryAvg': '77.16666666666667'
            }
        }

    """

    def dictToExcel(this, row, dict):
        #  dte.worksheet.write(0,pos, label=mstm.keyTheryAvgList[pos - 1])

        # print(dict)

        # 将学生姓名写到第一列
        # this.worksheet.write(row,0, label=dict.keys())

        # print(dict.keys())
        for key in dict.keys():
            this.worksheet.write(row, 0, key)

        for avgScore in dict.values():
            print(avgScore)
            print(len(avgScore))
            for pos in range(len(avgScore)):
                this.worksheet.write(row, pos + 1, float(avgScore[ScoreToMySQL.keyTheryAvgList[pos]]))

if __name__ == '__main__':

    mstm = ScoreToMySQL()

    dte = DictToExcel()

    dte.createNewSheetByName(mstm.keyTheryAvgList[0])

    dte.worksheet.write(0, 0, mstm.keySname)
    for pos in range(1, len(mstm.keyTheryAvgList) + 1):
        dte.worksheet.write(0, pos, mstm.keyTheryAvgList[pos - 1])

    fiveAvgList = mstm.selectFromFiveTimesThery(mstm.keyTheryAvgList[2])

    for line in range(1, len(fiveAvgList) + 1):
        dte.dictToExcel(line, fiveAvgList[line - 1])


    # 为数据添加柱形图

    """
    chart.add_series({
        'categories': '=Sheet1!$A$1:$A$5',
        'values':     '=Sheet1!$B$1:$B$5',
        'line':       {'color': 'red’},
        'name':'=各端BUG数汇总_图表!$A$3'
    })
    """


    mchart = dte.workbook.add_chart({"type": "column"})

    worksheet = dte.workbook.get_worksheet_by_name("{sheetname}".format(sheetname=mstm.keyTheryAvgList[0]))
    print(type(worksheet))

    mchart.add_series({
        'categories': '={sheetname}!R1C1:R{StudentCount}C1'.format(sheetname=mstm.keyTheryAvgList[0], StudentCount=dte.studentCount),
        'values': '={sheetname}!R1C5:R{StudentCount}C5'.format(sheetname=mstm.keyTheryAvgList[0], StudentCount=dte.studentCount),
        'line': {'color': 'red'},
        "name": "{seriesname}".format(seriesname=mstm.keyTheryAvgList[3])
    })
    mchart.add_series({
        'categories': '={sheetname}!R1C1:R{StudentCount}C1'.format(sheetname=mstm.keyTheryAvgList[0], StudentCount=dte.studentCount),
        'values': '={sheetname}!R1C4:R{StudentCount}C4'.format(sheetname=mstm.keyTheryAvgList[0], StudentCount=dte.studentCount),
        'line': {'color': 'red'},
        "name": "{seriesname}".format(seriesname=mstm.keyTheryAvgList[2])
    })
    mchart.add_series({
        'categories': '={sheetname}!R1C1:R{StudentCount}C1'.format(sheetname=mstm.keyTheryAvgList[0], StudentCount=dte.studentCount),
        'values': '={sheetname}!R1C3:R{StudentCount}C3'.format(sheetname=mstm.keyTheryAvgList[0], StudentCount=dte.studentCount),
        'line': {'color': 'red'},
        "name": "{seriesname}".format(seriesname=mstm.keyTheryAvgList[1])
    })
    mchart.add_series({
        'categories': '={sheetname}!R1C1:R{StudentCount}C1'.format(sheetname=mstm.keyTheryAvgList[0], StudentCount=dte.studentCount),
        'values': '={sheetname}!R1C2:R{StudentCount}C2'.format(sheetname=mstm.keyTheryAvgList[0], StudentCount=dte.studentCount),
        'line': {'color': 'red'},
        "name": "{seriesname}".format(seriesname=mstm.keyTheryAvgList[0])
    })

    mchart.set_style(10)
    mchart.height = 600
    mchart.width = 960

    worksheet.insert_chart('H2', mchart)

    dte.workbook.close()
