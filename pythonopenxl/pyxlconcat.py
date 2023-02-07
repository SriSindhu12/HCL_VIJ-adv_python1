from openpyxl import Workbook
from pandas import read_excel
sheet=[]
file='../data//sales.xlsx'
i=1
for f in ['JAN','FEB','MARCH','APRIL']:
    df=""
    name='HCL_SALES_'+f
    df=df+str(i)
    df=read_excel(file,name)
    i+=1
    sheet.append(df)
print(sheet)