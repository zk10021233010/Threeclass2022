# author:zhangkai
# time:'2022/2/28'
# --coding:utf-8-- \
import pytest,os
from tools.ExcelControl import get_excel_data
from lib.login import Login_class

# from configs.config import login_data,fail_data
# def test_login001():
#     res = Login_class().login(login_data)
#     # print(res)
#     assert res['code'] == '10000'
#     assert res['msg'] == 'success'
#
# def test_login002():
#     res = Login_class().login(fail_data)
#     # print(res)
#     assert  res['code'] == '20001'
#     assert  res['msg'] == '用户名或密码错误'
excelDir = f'../data/Threeclass_test.xls'
@pytest.mark.parametrize('tagName,inBody,expData',get_excel_data(excelDir,'校管理端','login'))
def test_login(tagName,inBody,expData):
    try:
        res = Login_class().login(inBody,getToken=False)
        assert res['code'] == expData['code']
        assert res['msg'] == expData['msg']
    except Exception as err:
        raise err

if __name__ == '__main__':
    # test_login001()
    # test_login002()
    pytest.main(['test_login.py','-s'])
    # pytest.main(['test_login.py','--alluredir','../report/tmp','-sq'])
    # os.system('allure serve ../report/tmp')