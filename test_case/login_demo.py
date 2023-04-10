# author:zhangkai
# time:'2022/2/23'
# --coding:utf-8--

import requests
# fiddler_proxies = {'http':'http://172.16.21.22:8888','https':'https://172.16.21.22:8888''}
HOST = 'http://threeclasses-test.web.qunlicloud.com/api'
login_data ={'userName':'18012340004','password':'Ql123123','catalog':'10','requestType':'web','verifyCodeToken':'null','authCode':'null'}
header={'LoginInPlatform':'school','Ql-Client-Id':'10'}

def login(inData):
    url=f'{HOST}/nsc/auth/login'
    payload = inData
    req = requests.post(url,data=payload,headers=header)
    return req.json()

def schoolUser_list(inData,pub_header):
    url=f'{HOST}/helpAdmin/schoolUserlist'
    payload = inData
    req= requests.post(url,json=payload,headers=pub_header)
    return req.json()

def chooseOrgToLogin(inData,org_header):
    url=f'{HOST}/personalCentre/chooseOrgToLogin'
    payload = inData
    req = requests.post(url, json=payload, headers=org_header)
    return req.json()

if __name__ == '__main__':
    # inData = login_data
    # res = login(inData)
    # print(res,'\n')
    # print(res['data']['access_token'])#通过字典的key取出对应value
    org_res = login(login_data)['data']
    print('登录接返回的data---：',org_res)
    token = org_res['access_token']
    print('获取的登录接口返回access_taken----:',token)
    res_org =org_res['orgs'][0]['organId']
    print('获取登录接口返回的orgId---:',res_org)
    req_header ={'LoginInPlatform':'school','Ql-Client-Id': '10','Authorization':'Bearer ' + token}#自定义请求头
    print('获取自定义的请求头是---：',req_header,'\n')
    choose_school = {'organId':res_org}
    res = chooseOrgToLogin(choose_school,req_header)
    print('选择登录学校的返回结果--:',res)
    inData2 = {"mobile":"","realName":"","pageNum":1,"pageSize":10,"orderBy":0}
    res2 = schoolUser_list(inData2,req_header)
    print('查询用户列表接口的结果是--:',res2)




