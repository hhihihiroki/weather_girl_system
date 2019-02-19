import xlrd


book = xlrd.open_workbook('地域コード改.xlsx')
sheet_1 = book.sheet_by_index(0)
        
data_dict = {}
    
for row_index in range(1,sheet_1.nrows):
    cell_name = sheet_1.cell(row_index, 6).value
    cell_code = sheet_1.cell(row_index, 7).value
    data_dict[cell_name] = cell_code
        