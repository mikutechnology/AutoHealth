'''
cron: 10 0 * * *
new Env('四川现代中台健康打卡_bcd');
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
        "auth" : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvbmVVc2VyIjp7ImlkIjoxNzAwOCwidXNlckFjY291bnQiOiI1MTE2MjMyMDAxMDQyODc0NzgiLCJ1c2VyUHdkIjoiMjg3NDc4IiwidXNlclBob25lIjoiIiwidXNlckVtYWlsIjoiIiwidXNlclF1YWwiOiIiLCJ1c2VyUm9sIjpudWxsLCJ1c2VyUXVhbElEIjo2LCJ1c2VyUmVnRGF0ZSI6IjIwMjAtMDktMjFUMDA6MDA6MDAiLCJwcm9DaGFubmVsIjoiIiwicHJvVXNlcklEIjoiIiwiaXNBZG1pbiI6IuWQpiIsInJvbE5hbWUiOm51bGwsInJvbERlc2NyaXB0aW9uIjpudWxsLCJyb2xEYXRlIjpudWxsLCJyb2xDcmVhdGVVc2VyIjpudWxsLCJjb21OYW1lIjpudWxsLCJjb21DbGFzcyI6bnVsbCwiY29tSUQiOm51bGwsImNvbUltZyI6bnVsbCwiY29tRmFSZW4iOm51bGwsImNvbVBob25lIjpudWxsLCJhZG1pbkVtYWlsIjpudWxsLCJhZG1pblBob25lIjpudWxsLCJ1c2VyU2hlbmciOm51bGwsInVzZXJTaGkiOm51bGwsInVzZXJYaWFuIjpudWxsLCJ1c2VyQWRkcmVzcyI6bnVsbCwicXVhbEFwcGx5RGF0ZSI6bnVsbCwicXVhbEFkb3BEYXRlIjpudWxsLCJxdWFsVXNlcklEIjpudWxsLCJpc1F1cmwiOm51bGwsIm9wZW5JRCI6Im9TZks1NVN3UWNjWkJ0Rnh5b1RYcjBadUxPWnMiLCJ1c2VySUQiOjE2MzUwLCJ1c2VyVHlwZSI6IuS4gOS6jOW5tOe6p-WtpueUnyIsInVzZXJDaGVjayI6IjUxMTYyMzIwMDEwNDI4NzQ3OCIsInVzZXJDaGVja1QiOiLljIXnlYXngp8iLCJkYXRhUm93cyI6IiIsImxpbmtSb3dzIjoiMzIifSwiSXNBZG1pbiI6ZmFsc2UsIkV4cGlyeURhdGVUaW1lIjoiMjAyMi0wNC0wNVQxODoxNzoxNS44MDM2NjI2KzA4OjAwIiwia2V5U3RyIjpudWxsLCJ2YWx1ZVN0ciI6bnVsbH0.BTTSUTdmMJJRRw5QjzH3leRdeqhykAm3-RvofJY5tww',
        "Content-Type": "application/json",
        "Referer": "https://servicewechat.com/wxb67ea4174221aa8f/5/page-frame.html",
        "Accept-Encoding": "gzip, deflate, br"
    }
# 将json类型的数据转换成字典类型的数据
data = ["一二年级学生",{"本人联系电话":"17628723617","家长联系电话":"13408265786","是否到过境外等地":"否","是否与境外等地接触":"否","本个人及家人是否接触新冠病例":"否","本个人及家人是否接触隔离者":"否","所属小区有无病例":"无","本人是否感染":"是","是否有以下症状":"无上述症状,","处理情况":"无","已准备口罩数":"","今日体温":"36.5","定位":"30.57447,103.92377"},4,"0","2","5,4,3"]

# 调用json.dumps()方法，将数据以json格式传递
response = requests.post(url=url,headers=headers, data=json.dumps(data))
result = response.text

print(result)
