import  xlrd
import  os

#exce文件默认行和列都是从1开始
# 在程序读取时是从0开始
# 因此需要将列值和行值减去1
excel_col_start_pos = 1
excel_row_start_pos = 1

#单选、多选和判断题的数量
single_answer_count = 20
mul_answer_count = 10
check_answer_count = 10

#标准答案所在列
excel_standard_answer_start_col = 3 - excel_col_start_pos

#单选题开始行
excel_single_answer_start_row = 5 - excel_row_start_pos
excel_single_answer_end_row = 5 - excel_row_start_pos + single_answer_count

#多选题开始行
excel_mul_answer_start_row = 27 - excel_row_start_pos
excel_mul_answer_end_row = 27 - excel_row_start_pos + mul_answer_count

#判断题开始行
excel_check_answer_start_row = 39 - excel_row_start_pos
excel_check_answer_end_row = 39 - excel_row_start_pos + check_answer_count

if __name__ == '__main__':

    propDestPath = r"D:\WEBProj\workspace\mycheckscoreproj"

    workbook = xlrd.open_workbook(r"./python1-week1-exam.xls")

    sheet = workbook.sheet_by_name("Sheet1")

    #读单选答案
    singleAnswerList = sheet.col_values(excel_standard_answer_start_col,
                     excel_single_answer_start_row,
                     excel_single_answer_end_row)

    print(singleAnswerList)

    #读多选答案
    mulAnswerList = sheet.col_values(excel_standard_answer_start_col,
                                        excel_mul_answer_start_row,
                                        excel_mul_answer_end_row)

    print(mulAnswerList)

    #读判断答案
    checkAnswerList = sheet.col_values(excel_standard_answer_start_col,
                                        excel_check_answer_start_row,
                                        excel_check_answer_end_row)

    print(checkAnswerList)

    #拼接属性文件的路径
    propPath = os.path.join(propDestPath, "score.txt")

    print(propPath)

    propFile = open(propPath, "w+")

    #将单选题答案写入到配置文件中
    propFile.write("singleAnswersStr=")

    pos = 0
    while True:
        mlen =  len(singleAnswerList)
        if pos == mlen :
            break

        propFile.write(singleAnswerList[pos])
        if pos < mlen-1 :
            propFile.write(",")

        pos+=1

    #给每个属性添加换行
    propFile.write("\n")

    #将多选题答案写入到配置文件中
    propFile.write("multiAnswersStr=")

    pos = 0
    while True:
        mlen =  len(mulAnswerList)
        if pos == mlen :
            break

        propFile.write(mulAnswerList[pos])
        if pos < mlen-1 :
            propFile.write(",")

        pos+=1


    #给每个属性添加换行
    propFile.write("\n")

    #将多选题答案写入到配置文件中
    propFile.write("chooseAnswersStr=")

    pos = 0
    while True:
        mlen =  len(checkAnswerList)
        if pos == mlen :
            break

        propFile.write(checkAnswerList[pos])
        if pos < mlen-1 :
            propFile.write(",")

        pos+=1




    propFile.close()

    # propPath = os.path.join(propDestPath, "score.txt")

    propNewPath = os.path.join(propDestPath, "score.properties")

    os.rename(propPath,propNewPath)
