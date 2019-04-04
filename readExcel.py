import xlrd

# wb=xlrd.open_workbook('./input/test_user_data.xlsx')
# sh=wb.sheet_by_name('TestUserLogin')
# 
# print(sh.nrows) # 行数
# print(sh.ncols) # 列数
# 
# print(sh.cell(0,0).value) # 打印第一行第一列的名字
# print(dict(zip(sh.row_values(0),sh.row_values(1))))
# 
# for i in range(sh.nrows):
#     print(sh.row_values(i))


def excel_to_list(data_file,sheet):
    data_list=[]
    wb=xlrd.open_workbook(data_file)
    sh=wb.sheet_by_name(sheet)
    header=sh.row_values(0)
    for i in range(1,sh.nrows):
        d=dict(zip(header,sh.row_values(i)))
        data_list.append(d)
    
    return data_list

def get_test_data(data_list,case_name):
    for case_data in data_list:
        if case_name == case_data["case_name"]:
            return case_data

# if __name__ == '__main__':
#     data_list=excel_to_list("./input/test_user_data.xlsx","TestUserLogin")
#     case_data=get_test_data(data_list, "test_user_login_normal")
#     print(case_data)     
    
    