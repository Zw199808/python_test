#
#
# import xlrd
#
#
# if __name__ == '__main__':
#     data = xlrd.open_workbook('/Users/zw/Desktop/化学院数据处理/1921_eduction_0.xlsx')
#     name = data.sheet_names() # 获取所有sheet的名字
#     table = []
#     print(name)
#     for i in range(len(name)):
#         table.append(data.sheet_by_name(name[i])) # 获取所有的列表
#
#
#     def getClassId(index): # 获取单个表中的class_id的值
#         ncols = table[index].ncols
#         return table[index].col_values(2,0,ncols)
#
#     value = getClassId(0)
#     print(value)
#
#
# import pandas as pd
#
# if __name__ == '__main__':
#     data = pd.read_excel('/Users/zw/Desktop/化学院数据处理/1921_eduction_0.xlsx')
#     print(data)