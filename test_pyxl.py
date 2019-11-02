import openpyxl, os
import datetime

filename = '/home/jszheng/Documents/test.xlsx'
f2 = 'date.xlsx'

def getdate(date):
    __s_date = datetime.date(1899, 12, 31).toordinal() - 1
    d = datetime.date.fromordinal(__s_date + date)
    return d

#print(os.path.isfile(filename))
wb = openpyxl.load_workbook(filename)
sheet = wb['Sheet1']
cell_1 = sheet['B1']
print(cell_1.value)
print(type(cell_1.value))

#a =datetime.date.fromordinal(cell_1.value)
#a = getdate(cell_1.value)
#print(a)

wb2 = openpyxl.load_workbook(f2)
s2 = wb2['Sheet']
c2 = s2['B1']
vc2 = c2.value
print(type(vc2))
print(vc2)