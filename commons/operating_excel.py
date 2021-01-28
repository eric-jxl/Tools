# -*- coding:utf-8 -*-
'''
@Author  : Eric
@Time    : 2021-01-15 15:28
@IDE     : PyCharm
'''
import xlrd
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

s =xlrd.open_workbook('../财务公司联系方式.xls')
data = s.sheet_by_index(0)._cell_values
data = data[4:]
lt = []
for rx in data:
    photo = str(rx[-2]).encode('utf-8').replace(' ','')
    lt.append(photo)
print lt