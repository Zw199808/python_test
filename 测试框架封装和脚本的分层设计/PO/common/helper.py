import xlrd
import logging, os

class Helper(object):

    def readExcel(self,rowx):
        # 读取表格

        book = xlrd.open_workbook('../data/datainfo.xlsx', 'r')
        table = book.sheet_by_index(0)
        return table.row_values(rowx)


    def readUsername(self,rowx):
        # 读取name
        return str(self.readExcel(rowx)[0])

    def readPassword(self,rowx):
        return str(self.readExcel(rowx)[1])

    def dirname(self,filename,filepath='data'):
        return os.path.join(os.path.dirname(os.path.dirname(__file__)),filepath,filename)