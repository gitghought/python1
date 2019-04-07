from myexcel.MyInclude import MyInclude
from myexcel.PickStudent import PickStudent
from myexcel.storetomysql import ScoreToMySQL
import xlwt
import xlrd

scoreExcelSrc = r"./{mclass}.xls".format(mclass = MyInclude.scoreExcelPrefix)

if __name__ == '__main__':

    #读取Excel文件前的准备工作
    mps = PickStudent(scoreExcelSrc)
    workBook = mps.myXlsOpen()
    sheet0 = mps.getSheetByName()

    for i in range(mps.studentScoreStartPos, mps.studentScoreStopPos):
        rowValues = mps.getRowValues(i)

        if mps.isNoneLine(rowValues) :
            pass
        else :
            pass

            # 将技能均分数据保存到数据库中
            # sname = mps.getStudentNameTuple()
            # print("sname = {sname}".format(sname=sname))
            #
            # listSkillAvgScore = []
            # dictSkillAvgScore = {}
            #
            # fiveDayAvgScore = mps.getFiveDaySkillAverageScoreTuple()
            # print("fiveDayAvgScore = {fiveDayAvgScore}".format(fiveDayAvgScore=fiveDayAvgScore))
            #
            # tenDayAvgScore = mps.getTenDaySkillAverageScoreTuple()
            # print("tenDayAvgScore = {tenDayAvgScore}".format(tenDayAvgScore=tenDayAvgScore))
            #
            # fifteenDayAvgScore = mps.getFifteenDaySkillAverageScoreTuple()
            # print("fifteenDayAvgScore = {fifteenDayAvgScore}".format(fifteenDayAvgScore=fifteenDayAvgScore))
            #
            # monthAvgScore = mps.getMonthSkillAverageScoreTuple()
            # print("monthAvgScore = {monthAvgScore}".format(monthAvgScore=monthAvgScore))
            #
            #
            # listSkillAvgScore.append(sname)
            # listSkillAvgScore.append(fiveDayAvgScore)
            # listSkillAvgScore.append(tenDayAvgScore)
            # listSkillAvgScore.append(fifteenDayAvgScore)
            # listSkillAvgScore.append(monthAvgScore)
            #
            #
            # dictSkillAvgScore = dict(listSkillAvgScore)
            #
            # print(dictSkillAvgScore)
            #
            # mstm = ScoreToMySQL()
            #
            # # 将准备的字典数据添加到数据库
            # mstm.insertIntoFiveTimesSkillDict(dictSkillAvgScore)
            #
            # # 关闭本次数据库连接
            # mstm.disConnect()


            # 将理论均分数据保存到数据库中
            listTheryAvgScore = []
            dictTheryAvgScore = {}

            sname = mps.getStudentNameTuple()

            fiveDayAvgScore = mps.getFiveDayTheryAverageScoreTuple()
            print("fiveDayAvgScore = {fiveDayAvgScore}".format(fiveDayAvgScore=fiveDayAvgScore))

            tenDayAvgScore = mps.getTenDayTheryAverageScoreTuple()
            print("tenDayAvgScore = {tenDayAvgScore}".format(tenDayAvgScore=tenDayAvgScore))

            fifteenDayAvgScore = mps.getFifteenDayTheryAverageScoreTuple()
            print("fifteenDayAvgScore = {fifteenDayAvgScore}".format(fifteenDayAvgScore=fifteenDayAvgScore))

            monthAvgScore = mps.getMonthTheryAverageScoreTuple()
            print("monthAvgScore = {monthAvgScore}".format(monthAvgScore=monthAvgScore))

            listTheryAvgScore.append(sname)
            listTheryAvgScore.append(fiveDayAvgScore)
            listTheryAvgScore.append(tenDayAvgScore)
            listTheryAvgScore.append(fifteenDayAvgScore)
            listTheryAvgScore.append(monthAvgScore)
            listTheryAvgScore.append(ScoreToMySQL.getClassTuple(MyInclude.scoreExcelPrefix))

            dictTheryAvgScore = dict(listTheryAvgScore)

            print("dictTheryAvgScore = " + str(dictTheryAvgScore))

            mstm = ScoreToMySQL()

            # 将准备的字典数据添加到数据库
            mstm.insertIntoFiveTimesTheryDict(dictTheryAvgScore)

            # 关闭本次数据库连接
            mstm.disConnect()


