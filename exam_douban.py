# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:57:16 2019

@author: l50004076
"""
import urllib
from bs4 import BeautifulSoup


def get_content(url , data = None):
    with urllib.request.urlopen(url) as response:
        html = response.read().decode("utf-8")
    return html


def get_data(html_text):
    infos = []
    bs = BeautifulSoup(html_text, "html.parser")  # 创建BeautifulSoup对象
    body = bs.body # 获取body部分
    block = body.find('ul', {'class': 'chart-dashed-list'})  # 找到排行表格
    items = block.find_all('li')  # 获取所有的li

    for item in items: # 对每个li标签中的内容进行遍历
        rank = item.find("strong", {"class": "fleft green-num-box"}).string
        name = item.find("a", {"class": "fleft"}).string
        score = item.find("span", {"class": "font-small color-red fleft"}
            ).string
        cover_url = item.find("img").attrs["src"]
        infos.append([rank, name, score, cover_url])
    return infos




if __name__ == '__main__':
    url ='https://book.douban.com/chart?subcat=F'
    html_text = get_content(url)
    result = get_data(html_text)
    
    for item in result:
        rank, name, score, cover_url = item
        fig_name = f'{rank}_{name}_{score}.jpg'
        imgres = urllib.request.urlopen(cover_url).read()
        with open(fig_name, "wb") as f: f.write(imgres)