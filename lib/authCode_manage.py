# author:zhangkai
# time:'2022/3/3'
# --coding:utf-8--

import requests
from configs.config import HOST,login_data,authCode_data
from lib.login import Login_class

class authCode_mge_class:
    # def __init__(self):
    #     inData = login_data
    #     self.header = Login_class().login(inData,getToken=True)

    #运行case使用
    def __init__(self,inToken):
        self.Authorization = inToken

    def  auth_Code_list(self,indata):
        url = f'{HOST}/authCodeSchool/authCodeList'
        payload = indata
        try:
            r = requests.post(url,json=payload,headers=self.Authorization)
            return r.json()
        except:
            print('程序错误')
            return 'error'

if __name__ =='__main__':
    indata = authCode_data
    res = authCode_mge_class().auth_Code_list(indata)
    print(res)