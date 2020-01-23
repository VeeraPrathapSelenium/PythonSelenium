import xlrd

path=r"C:\Users\Hanshik\Desktop\Testadata.xlsx"

workbook=xlrd.open_workbook(path)

cellvalue=workbook.sheet_by_name("Data").cell_value(0,0)

totalrows=workbook.sheet_by_name("Data").nrows
print(totalrows)
totalcols=workbook.sheet_by_name("Data").ncols
print(totalcols)


for r in range(0,totalrows):

    for c in range(0,totalcols):

        data=workbook.sheet_by_name("Data").cell_value(int(r),int(c))
        print(data)

