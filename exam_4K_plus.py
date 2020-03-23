# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 21:45:31 2020

@author: Sean
"""
import exam_4K as e4k
from bs4 import BeautifulSoup

# homepage
html_text = e4k.get_content(e4k.HOME_URL, e4k.REQ_HEADER)

# extract sub tags
bs = BeautifulSoup(html_text.decode("utf-8"), "html.parser")  # 创建BeautifulSoup对象
body = bs.body # 获取body部分
blocks = body.find('div', {'class': 'home_tag'}).find_all('a')  # 获取所有的tags
urls = [(block.attrs["title"], block.attrs["href"]) for block in blocks]
for i_tag, (title, tag_url) in enumerate(urls):
    print("=" * 30)
    print(f"{tag_url:-^30}")
    print(f"{len(urls)}-{i_tag+1}")
    for i_try in range(3):
        try:
            e4k.run(tag_url)
            break
        except:
            print("tag failed!")
            

