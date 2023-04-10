# author:zhangkai
# time:'2022/3/1'
# --coding:utf-8--

import xlrd,json

def get_excel_data(excelDir,sheetName,caseName):
    reslist =[] #存放Excel ----方局部变量，每次存过以后用完就清理掉
    #1- 获取excel 路径
    # excelDir = f'../data/Threeclass_ttestcase.xlsx'
    #2- 需要把 excel 加载到内存 ----open-----format_info=True 保持原样式
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)
    #3- 获取对应的sheet
    print(workBook.sheet_names()) #获取所有的 sheet 名称
    workSheet = workBook.sheet_by_name(sheetName)
    idx = 0 #遍历变量
    for one in workSheet.col_values(0):
        if caseName in one:
            tagName = workSheet.cell(idx,0).value #用例编号
            reqBodyData = workSheet.cell(idx,9).value #请求体
            respData = workSheet.cell(idx,11).value #响应体
            #接口要传递的是字典格式。 excel读取是str，需要
            reslist.append((tagName,json.loads(reqBodyData),json.loads(respData)))
        idx += 1
    return reslist
if __name__ == '__main__':
    excelDir = f'../data/Threeclass_test.xls'
    res = get_excel_data(excelDir,'校管理端','login')
    # print(res)
    for one in res:
        print(one,'\n')