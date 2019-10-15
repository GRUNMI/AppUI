# coding:utf-8
__author__ = 'GRUNMI'


import xlrd
import os
from AppAuto.common.LogOutput import Log


PATH = lambda P: os.path.abspath(os.path.join(os.path.dirname(__file__), P))
mylogger = Log().get_logger()


class ReadXLSX:
    def __init__(self, sheetName):
        self.xlsxPath = PATH("../ConfigData/CaseData.xlsx")
        self.sheetName = sheetName

    def read_xlsxData(self, cell=None, row=None, col=None):
        ''''
        :cell 标识单元格
        rowx、colx 标识单元格数字
        eg: cell='A1'
            rowx=1, colx=1
        优先cell
        '''
        workbook = xlrd.open_workbook(self.xlsxPath)
        sheet = workbook.sheet_by_name(self.sheetName)
        try:
            if cell:
                col = {
                    'A': 0,
                    'B': 1,
                    'C': 2,
                    'D': 3,
                    'E': 4,
                    'F': 5,
                    'G': 6,
                    'H': 7,
                    'I': 8,
                    'J': 9,
                    'K': 10,
                    'L': 11,
                    'M': 12,
                    'N': 13,
                    'O': 14,
                    'P': 15,
                    'Q': 17,
                    'R': 18,
                    'S': 19,
                    'T': 20,
                    'U': 21,
                    'V': 22,
                    'W': 23,
                    'Y': 24,
                    'Z': 25,
                }
                # 去掉输入的空格
                cellVale = []
                for i in cell:
                    for x in i:
                        if x != '':
                            cellVale.append(x)
                # 获取row和col
                rows = []
                cols = []
                for i in cellVale:
                    try:
                        if int(i):
                            rows.append(i)
                    except:
                        cols.append(i)
                # 设置row和col减1，原cell从0开始
                val = sheet.cell(colx=col[''.join(cols).upper()], rowx=int(''.join(rows))-1)
            else:
                # 设置row和col减1，原cell从0开始
                val = sheet.cell(colx=int(col)-1, rowx=int(row)-1)

            ctype = val.ctype
            value = val.value
            # ctype==2 为浮点型 value % 1 余数
            if ctype == 2 and value % 1 == 0.0:
                mylogger.info("获取值为 {}".format(str(int(value))))
                return str(int(value))
            mylogger.info("获取值为 {}".format(str(value)))
            return str(value)

            # 判断value不能为空，因存在不输入的情况，所以不能返回None
            # if len(value) > 0:
            #     mylogger.info("获取值为 {}".format(str(value)))
            #     return str(value)
            # else:
            #     mylogger.info("单元格为空 {}".format(value))
            #     return None
        except Exception as e:
            mylogger.info("单元格为空 {}".format(e))
            return None

if __name__ == '__main__':
    data = ReadXLSX("page_ele")
    data.read_xlsxData(cell='d11')
