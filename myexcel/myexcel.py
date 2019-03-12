
import xlrd

from datetime import date,datetime

single_num = 20
mul_num = 10
pan_num = 10

def read_student_excel():

    #指定学生答案在第几列
    student_answer_pos = 1

    single_answer = []
    single_start_pos = 4

    mul_answer = []
    mul_start_pos = 26

    pan_answer = []
    pan_start_pos = 38

    #存储学生答案的数据结构
    student_answer = {"single_answer":[], "mul_answer":[], "pan_answer":[]}

    #文件位置
    ExcelFile=xlrd.open_workbook(r'F:\PycharmProjects\python1\myexcel\answer.xls')

    #获取第一个表格的对象
    sheet=ExcelFile.sheet_by_name('Sheet1')

    #单选回答
    single_answer=sheet.col_values(student_answer_pos, single_start_pos, single_start_pos+single_num)#第二列内容
    # print(single_answer)
    # print(len(single_answer))
    student_answer["single_answer"] = single_answer

    #多选回答
    mul_answer=sheet.col_values(student_answer_pos, mul_start_pos, mul_start_pos+mul_num)#第二列内容
    # print(mul_answer)
    # print(len(mul_answer))
    student_answer["mul_answer"] = mul_answer

    #判断回答
    pan_answer=sheet.col_values(student_answer_pos, pan_start_pos, pan_start_pos+pan_num)#第二列内容
    # print(pan_answer)
    # print(len(pan_answer))
    student_answer["pan_answer"] = pan_answer

    return student_answer

def read_teacher_excel () :
    #指定学生答案在第几列
    student_answer_pos = 1

    single_answer = []
    single_start_pos = 4
    single_num = 20

    mul_answer = []
    mul_start_pos = 26
    mul_num = 10

    pan_answer = []
    pan_start_pos = 38
    pan_num = 10

    #存储学生答案的数据结构
    student_answer = {"single_answer":[], "mul_answer":[], "pan_answer":[]}

    #文件位置
    ExcelFile=xlrd.open_workbook(r'F:\PycharmProjects\python1\myexcel\a.xls')

    #获取目标EXCEL文件sheet名
    print(ExcelFile.sheet_names())

    #获取第一个表格的对象
    sheet=ExcelFile.sheet_by_name('Sheet1')

    #单选回答
    single_answer=sheet.col_values(student_answer_pos, single_start_pos, single_start_pos+single_num)#第二列内容
    # print(single_answer)
    # print(len(single_answer))
    student_answer["single_answer"] = single_answer

    #多选回答
    mul_answer=sheet.col_values(student_answer_pos, mul_start_pos, mul_start_pos+mul_num)#第二列内容
    # print(mul_answer)
    # print(len(mul_answer))
    student_answer["mul_answer"] = mul_answer

    #判断回答
    pan_answer=sheet.col_values(student_answer_pos, pan_start_pos, pan_start_pos+pan_num)#第二列内容
    # print(pan_answer)
    # print(len(pan_answer))
    student_answer["pan_answer"] = pan_answer

    return student_answer

def check_single(teacher , student) :
    # print(teacher)
    # print(student)

    #获取单选选项答案
    # print(type(teacher))
    teacher_single_answer = teacher["single_answer"]
    # print(teacher_single_answer)

    student_single_answer = student["single_answer"]
    # print(student_single_answer)

    # question_serialized = [for t in teacher_single_answer for s in student_single_answer]
    question_serialized = list()
    print(len(question_serialized))

    mpos = 0
    while True:
        if teacher_single_answer[mpos] == student_single_answer[mpos] :
            # question_serialized[mpos] = True
            question_serialized.append(True)
        else :
            question_serialized.append(False)

        mpos += 1
        if mpos >= single_num :
            break

    print(question_serialized)
    print(len(question_serialized))


if __name__ == '__main__':
    stu = read_student_excel()
    # print(stuanw)
    te = read_teacher_excel()
    # print(te)

    check_single(te, stu)

