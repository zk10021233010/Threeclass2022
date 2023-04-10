# import pytest
# import os
# import allure
# #2.封装测试类
# class TestLogin: #登录模块
#     #该测试类--前置操作--初始化
#     def setup_class(self):
#         print('执行测试之前，我需要执行')
#
#     def test_login01(self):
#         print('----test_login01----')
#         assert 1 + 1 == 2
#
#     # def test_login02(self):
#     #     print('----test_login02----')
#     #     assert 1+1 == 3
#
#     #该测试类--清除操作--初始化
#     def teardown_class(self):
#         pring('----该测试类的环境清除----')
#
# #测试用例执行操作
# if __name__ == '__main__':
#     #需要打印对应的信息 -s
#     #1 --alluredir 存放目录
#     # pytest.main(['test_func01.py','-s','--alluredir','../report/tmp'])
#     # # #2 allure generate 报告 allure报告 cmd指令---os.system()
#     # # #os.('allure generate 报告需要的数据 -o 报告存放的目录 --clean‘)
#     # os.system('allure generate ../report/tmp -o ../report/report --clean')
