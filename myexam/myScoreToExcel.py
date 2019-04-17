import  xlsxwriter
import  os
import json

def isTxt(filename) :
    return str(filename).endswith(".txt")


if __name__ == '__main__':

    # fileScorePath = r"D:\checkscore\test\"

    fileScorePath = os.path.join("D:", "checkscore", "test")
    # print(fileScorePath)

    filePath = "."
    fileName = "score.xls"

    filePathName = os.path.join(filePath, fileName)

    workbook = xlsxwriter.Workbook(filePathName)

    sheet = workbook.add_worksheet("python1")


    excel_start_row = 1
    excel_start_col = 1

    excel_score_start_row = 1 - excel_start_row

    excel_score_name_start_col = 1 - excel_start_col
    excel_score_score_start_col = 2 - excel_start_col
    pos = 0


    propDestPath = r"D:\checkscore\test"

    fileList = os.listdir(propDestPath)

    fileTxt = filter(isTxt, fileList)

    for f in fileTxt:
        #拼接学生成绩文件的路径
        fpath = os.path.join(fileScorePath, f)

        # 打开每一个学生成绩单文件
        file = open(fpath, "rb")

        # 读取当前文件的所有行
        flist = file.readlines()

        # print(type(flist[3].decode("utf-8")))

        #单独解析成绩单中最后一行的数据
        # 最后一行是理论总分
        j = json.loads(str(flist[3].decode("utf-8")))
        print(type(j.keys()))

        """
        def write(self,
          row: {__lt__, __ge__, __gt__},
          col: {__lt__, __ge__},
          *args: Any) -> Any
        
        """
        sheet.write(excel_score_start_row + pos,
                    excel_score_name_start_col,
                    list(j.keys())[0])

        sheet.write(excel_score_start_row + pos,
                    excel_score_score_start_col,
                    list(j.values())[0])

        pos += 1



        file.close()

    workbook.close()

