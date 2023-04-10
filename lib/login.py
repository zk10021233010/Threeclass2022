# author:zhangkai
# time:'2022/2/28'
# --coding:utf-8--

import requests
from configs.config import HOST,login_data

class Login_class:
    #该测试类--前置操作--初始化

    # def __int__(self,Token):#运行用例使用

    def __init__(self):
        self.header = {'LoginInPlatform':'school','Ql-Client-Id':'10'}#本模块调试用、

    def login(self,inData,getToken=None):
        url = f'{HOST}/nsc/auth/login'
        payload = inData
        try:
            r = requests.post(url,data=payload,headers = self.header)
            if getToken:
                return {'LoginInPlatform':'school','Ql-Client-Id':'10','Authorization':'Bearer '+r.json()['data']['access_token']}
            else:
                return r.json()
        except:
            print('程序错误')


if __name__ == '__main__':
    inData = login_data
    res = Login_class().login(inData,getToken=False)
    if res['code'] == '10000':
        print('pass')
    else:
        print('fail')
    print(res)








