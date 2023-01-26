'''
new Env('四川现代中台健康打卡_xxx');
'''
# 第一行xxx填写你的姓名简写拼音
import requests
import json
url = 'https://www.scmvcweb.cn/UserAPI/wxSaveTableData'
headers = {
        "Host" : "www.scmvcweb.cn",
        "Connection": "keep-alive",
        "Content-Length": "480",
        "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        # auth是www.scmvcweb.cn的cookie，需手动抓取
        "auth" : 'xxx',
        "Content-Type": "application/json",
        "Referer": "https://servicewechat.com/wxb67ea4174221aa8f/5/page-frame.html",
        "Accept-Encoding": "gzip, deflate, br"
    }
# 将json类型的数据转换成字典类型的数据
data = ["一二年级学生",{"本人联系电话":"xxx","家长联系电话":"xxx","是否到过境外等地":"否","是否与境外等地接触":"否","本个人及家人是否接触新冠病例":"否","本个人及家人是否接触隔离者":"否","所属小区有无病例":"无","本人是否感染":"是","是否有以下症状":"无上述症状,","处理情况":"无","已准备口罩数":"","今日体温":"36.5","定位":"30.57447,103.92377"},4,"0","2","5,4,3"]

# 调用json.dumps()方法，将数据以json格式传递
response = requests.post(url=url,headers=headers, data=json.dumps(data))
result = response.text

print(result)