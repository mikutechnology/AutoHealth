'''
cron: 15 0 * * *
new Env('四川现代中台健康打卡_bzl');
'''
import requests
import json
url = 'https://www.scmvcweb.cn/UserAPI/wxSaveTableData'
headers = {
        "Host" : "www.scmvcweb.cn",
        "Connection": "keep-alive",
        "Content-Length": "480",
        "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "auth" : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvbmVVc2VyIjp7ImlkIjoxNjAyOCwidXNlckFjY291bnQiOiI1MTA1MjIyMDAxMDkxNjAwMTkiLCJ1c2VyUHdkIjoiMTYwMDE5IiwidXNlclBob25lIjoiIiwidXNlckVtYWlsIjoiIiwidXNlclF1YWwiOiIiLCJ1c2VyUm9sIjpudWxsLCJ1c2VyUXVhbElEIjo2LCJ1c2VyUmVnRGF0ZSI6IjIwMjAtMDktMjFUMDA6MDA6MDAiLCJwcm9DaGFubmVsIjoiIiwicHJvVXNlcklEIjoiIiwiaXNBZG1pbiI6IuWQpiIsInJvbE5hbWUiOm51bGwsInJvbERlc2NyaXB0aW9uIjpudWxsLCJyb2xEYXRlIjpudWxsLCJyb2xDcmVhdGVVc2VyIjpudWxsLCJjb21OYW1lIjpudWxsLCJjb21DbGFzcyI6bnVsbCwiY29tSUQiOm51bGwsImNvbUltZyI6bnVsbCwiY29tRmFSZW4iOm51bGwsImNvbVBob25lIjpudWxsLCJhZG1pbkVtYWlsIjpudWxsLCJhZG1pblBob25lIjpudWxsLCJ1c2VyU2hlbmciOm51bGwsInVzZXJTaGkiOm51bGwsInVzZXJYaWFuIjpudWxsLCJ1c2VyQWRkcmVzcyI6bnVsbCwicXVhbEFwcGx5RGF0ZSI6bnVsbCwicXVhbEFkb3BEYXRlIjpudWxsLCJxdWFsVXNlcklEIjpudWxsLCJpc1F1cmwiOm51bGwsIm9wZW5JRCI6Im9TZks1NVdiVFRsZHVvVHdfNERLMVpVSTctYUEiLCJ1c2VySUQiOjE1MzcwLCJ1c2VyVHlwZSI6IuS4gOS6jOW5tOe6p-WtpueUnyIsInVzZXJDaGVjayI6IjUxMDUyMjIwMDEwOTE2MDAxOSIsInVzZXJDaGVja1QiOiLljZ7mraPmt4siLCJkYXRhUm93cyI6IiIsImxpbmtSb3dzIjoiMzIifSwiSXNBZG1pbiI6ZmFsc2UsIkV4cGlyeURhdGVUaW1lIjoiMjAyMi0wNC0wMVQxOToyNjoxOS40Nzc1MTg2KzA4OjAwIiwia2V5U3RyIjpudWxsLCJ2YWx1ZVN0ciI6bnVsbH0.ulEygbA4gu_B04gBSo8b-aDgvIhPzTxl9aJVsXc4-DU',
        "Content-Type": "application/json",
        "Referer": "https://servicewechat.com/wxb67ea4174221aa8f/5/page-frame.html",
        "Accept-Encoding": "gzip, deflate, br"
    }
# 将json类型的数据转换成字典类型的数据
data = ["一二年级学生",{"本人联系电话":"18011045196","家长联系电话":"18011046156","是否到过境外等地":"否","是否与境外等地接触":"否","本个人及家人是否接触新冠病例":"否","本个人及家人是否接触隔离者":"否","所属小区有无病例":"无","本人是否感染":"是","是否有以下症状":"无上述症状,","处理情况":"无","已准备口罩数":"","今日体温":"36.5","定位":"30.57447,103.92377"},4,"0","2","5,4,3"]

# 调用json.dumps()方法，将数据以json格式传递
response = requests.post(url=url,headers=headers, data=json.dumps(data))
result = response.text

print(result)