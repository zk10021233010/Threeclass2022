# author:zhangkai
# time:2022/3/4
# -*-coding:utf-8-*-

import pytest,os
@pytest.fixture(scope='session',autouse=True )#加上autouse=Ture代表用例执行前自动运行下面的方法：
def start_running():
    print('----接口自动化运行开始----')

    #测试报告数据清除
    try:
        for one in os.listdir('../report/tmp'):
            if 'json' in one or 'txt' in one:#多种文件可用or if 'josn' or 'jpg' in one
                # print(one)
                os.remove(f'../report/tmp/{one}')
        print('清除tmp目录')
    except:
        print('第一次执行pytest框架')
    yield #用例全部执行完后执行--相当于teardown用法
    print('----接口自动化运行完成-----')

#========================初始化登录鉴权获取access_token======================
@pytest.fixture(scope='class')
def login_init():
    from lib.login import Login_class
    from configs.config import login_data
    login_token = Login_class().login(login_data,getToken=True)
    return login_token
c
#初始化授权码管理模块
from lib.authCode_manage import authCode_mge_class
@pytest.fixture(scope='class')
def auth_code_init(login_init):
    auth_code =authCode_mge_class(login_init)
    return auth_code
