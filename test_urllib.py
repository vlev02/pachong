# -*- coding: utf-8 -*-
"""我在菊厂学爬虫——urllib"""
import urllib


def proxy_init():
    """代理配置"""
    proxy_support = urllib.request.ProxyHandler(
        {'http': 'http://l50004076:lx271133.@proxycn2.huawei.com:8080',
         'https': 'http://l50004076:lx271133.@proxycn2.huawei.com:8080'})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)


def request1():
    """urlopen 示例"""
    response = urllib.request.urlopen(r"https://www.python.org")
    print(response.read().decode("utf-8"))
    response.close()


def request2():
    """status，reason，getheaders 示例"""
    with urllib.request.urlopen(r"https://www.python.org") as f:
        print('Status:', f.status, f.reason)
        for k, v in sorted(f.getheaders()):
            print('%s: %s' % (k, v))


def request3():
    """参数data 示例"""
    data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
    with urllib.request.urlopen(r"http://httpbin.org/post", data=data) as f:
        print('Status:', f.status, f.reason)
        for k, v in sorted(f.getheaders()):
            print(f'{k}:\n\t{v:}\n')
        print(f.read().decode("utf-8"))


def request4():
    """urllib.error 处理异常"""
    try:
        urllib.request.urlopen('http://cuiqingcai.com/index.htm')
    except urllib.error.URLError  as e:
        print(e.reason, e.code, e.headers, sep='\n')
    except urllib.error.HTTPError as e:
        print(e.reason, e.code, e.headers, sep='\n')
    else:
        print("Request Successfully")
    finally:
        pass


def main():
    proxy_init()
    request4()


if __name__ == "__main__":
    main()
