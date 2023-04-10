# author:zhangkai
# time:'2022/3/4'
# --coding:utf-8--
import pytest,os

if __name__ == '__main__':
    #修改根目录
    pytest.main(['--alluredir','../report/tmp','-sq'])
    #执行命令 allure generate ./tmp -o ./report --clean
    os.system('allure generate ../ report/tmp -o ../report/report --clean')