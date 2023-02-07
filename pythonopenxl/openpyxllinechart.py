from openpyxl import Workbook
from openpyxl.chart import Reference,LineChart
sales_data=[["year","sales"],[2010,1000],[2011,9000],[2012,2000],[2013,4000],[2014,5000]]
wb=Workbook()
sheet=wb.active
for row in sales_data:
    sheet.append(row)
chart=LineChart()
data=Reference(worksheet=sheet,min_row=1,max_row=8,min_col=2,max_col=3)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"H2")
wb.save("..//data/chart2.xlsx")
