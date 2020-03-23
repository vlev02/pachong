# -*- coding: utf-8 -*-
"""我在菊厂学爬虫——requests"""
import requests


# =============================================================================
response  = requests.get("https://www.baidu.com")
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)
print(response.content)
print(response.content.decode("utf-8"))


# =============================================================================
# 各种请求
# =============================================================================
requests.post("http://httpbin.org/post")
requests.put("http://httpbin.org/put")
requests.delete("http://httpbin.org/delete")
requests.head("http://httpbin.org/get")
requests.options("http://httpbin.org/get")


# =============================================================================
# params
# =============================================================================
data = {
    "name":"zhaofan",
    "age":22
}
response = requests.get("http://httpbin.org/get",params=data)
print(response.url)
print(response.text)


# =============================================================================
# json
# =============================================================================
import json
response = requests.get("http://httpbin.org/get")
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))


# =============================================================================
# 添加headers
# =============================================================================
# 在谷歌浏览器里输入chrome://version
agent = r"""Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 """ \
        r"""(KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"""
headers = {"User-Agent":agent}
response =requests.get("https://www.zhihu.com",headers=headers)
print(response.text)


# =============================================================================
# 基本POST请求
# =============================================================================
data = {"name":"zhaofan", "age":23}
response = requests.post("http://httpbin.org/post",data=data)
print(response.text)


# =============================================================================
# response
# =============================================================================
response = requests.get("http://www.baidu.com")
print(type(response.status_code),response.status_code)
print(type(response.headers),response.headers)
print(type(response.cookies),response.cookies)
print(type(response.url),response.url)
print(type(response.history),response.history)


# =============================================================================
# 获取cookie
# =============================================================================
response = requests.get("http://www.baidu.com")
print(response.cookies)
for key,value in response.cookies.items():
    print(key+"="+value)


# =============================================================================
# 会话维持
# =============================================================================
with requests.Session() as s:
    s.get("http://httpbin.org/cookies/set/number/123456")
    response = s.get("http://httpbin.org/cookies")
    print(response.text)


# =============================================================================
# 证书验证
# =============================================================================
from requests.packages import urllib3
urllib3.disable_warnings()
response = requests.get("https://www.12306.cn",verify=False)
print(response.status_code)












