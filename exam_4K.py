# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 10:37:49 2020

@author: Sean
"""
import os
import urllib
import requests
from bs4 import BeautifulSoup


FIG_SAVE_DIR = r"C:\Users\Sean\Pictures\Saved Pictures"  # 图片存储路径
HOME_URL = r"https://uhdpixel.com/"
#HOME_URL = r"https://uhdpixel.com/wall/tag/batgirl-dc/"
REQ_HEADER =  {'User-Agent': r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
FIG_HEADER = {"referer": "https://uhdpixel.com/wall/mountains-forest-minimalist-minimalism-4k-y7113/",
              "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

def get_content(url, header=None):
    # 增加请求头
    if header is not None:
        page_h = urllib.request.Request(url, headers=header)
        page = urllib.request.urlopen(page_h, timeout=5)
        html=page.read()
        return html

    # 基本请求
    with urllib.request.urlopen(url) as response:
        html = response.read()
    return html


def home_page_extract(html_text):
    """提取主页的所有图片链接"""
    bs = BeautifulSoup(html_text.decode("utf-8"), "html.parser")  # 创建BeautifulSoup对象
    body = bs.body # 获取body部分
    blocks = body.find_all('div', {'class': 'thumb_con'})  # 获取所有的li
    urls = [block.find('a').attrs["href"] for block in blocks]
    return urls

def jpg_url_extract(fig_page):
    """提取图片页面的图片资源链接"""
    bs = BeautifulSoup(fig_page.decode("utf-8"), "html.parser")  # 创建BeautifulSoup对象
    body = bs.body # 获取body部分
    block = body.find('div', {'class': 'wp_dl'})  # 获取div
    fig_source = block.find('a').attrs["href"]
    return fig_source
    
    
    
def fig_download(fig_urls, header=None):
    """下载指定链接的图片"""
    for i, fig_url in enumerate(fig_urls):
        print(f"fig[{len(fig_urls)}-{i+1}]")
        try_num = 3
        while try_num:
            try:
                fig_page = get_content(fig_url, header=header)
                fig_source = jpg_url_extract(fig_page)
                break
            except:
                print(f"jpg_url_extract failed!")
                try_num -= 1
                
        fig_name = os.path.join(FIG_SAVE_DIR, f"{fig_source.split('/')[-1]}")
        if os.path.isfile(fig_name):
            print(f"[{fig_name}] exist!")
            continue
            
        print(f"downloading [{fig_name}]")
        try_num = 3
        while try_num:
            try:
                # key!!!
                html = requests.get(fig_source, headers=FIG_HEADER)
                with open(fig_name, 'wb') as f:
                    f.write(html.content)
                # key!!!
                break
            except:
                print(f"download failed!")
                try_num -= 1
        print("success!")
    
def run(tag_url):
    html_text = get_content(tag_url, REQ_HEADER)
    fig_urls = home_page_extract(html_text)
    fig_download(fig_urls, header=REQ_HEADER)
    
if __name__ =="__main__":
    html_text = get_content(HOME_URL, REQ_HEADER)
    fig_urls = home_page_extract(html_text)
    fig_download(fig_urls, header=REQ_HEADER)
    pass
    
    
    
    
    
    
    
    