# author:zhangkai
# time:'2022/3/4'
# --coding:utf-8--
import pytest,time,os
from lib.authCode_manage import authCode_mge_class
from tools.ExcelControl import get_excel_data
from lib.login import Login_class
from configs.config import login_data


excelDir = f'../data/Threeclass_test.xls'
class Test_authCode:
    def setup_class(self):
        self.token = Login_class().login(login_data,getToken=True)

    @pytest.mark.parametrize('tagName,inBody,expData',get_excel_data(excelDir,'校管理端','authCode'))
    def test_authCode_list(self,tagName,inBody,expData,auth_code_init):
        try:
            res = auth_code_init.auth_Code_list(inBody)
            time.sleep(1)
            assert res['code'] == expData['code']
        except Exception as err:
            raise err

if __name__ == '__main__':
    # test_login001()
    # test_login002()
    # pytest.main(['test_authCode.py','-s'])
    pytest.main(['test_authCode.py','--alluredir','../report/tmp','-sq'])
    # os.system('allure serve ../report/tmp')
    os.system('allure generate ../report/tmp -o ../report/report --clean')
