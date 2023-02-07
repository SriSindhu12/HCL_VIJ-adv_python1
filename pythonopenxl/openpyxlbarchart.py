from openpyxl import Workbook
from openpyxl.chart import Reference,BarChart
sales_data=[["product","online","store"],[1,30,40],[2,40,50],[3,45,55],[4,55,34],[5,56,65]]
wb=Workbook()
sheet=wb.active
for row in sales_data:
    sheet.append(row)
chart=BarChart()
data=Reference(worksheet=sheet,min_row=1,max_row=8,min_col=2,max_col=3)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"H2")
wb.save("..//data/chart.xlsx")
