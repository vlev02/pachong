"""being 壁纸下载"""
import re
import os
import requests
from bs4 import BeautifulSoup


HOME_URL = r"https://www.prohui.com/bing"  # 主页
FIG_DIR = r"C:\Users\Sean\Pictures\Saved Pictures"  # 图片存储路径


response  = requests.get(HOME_URL)
bf_body = BeautifulSoup(response.content, "html.parser")  # .body
fig_url = bf_body.find("span", {"class": "y"}).find("a").attrs["href"]

fig_html = requests.get(fig_url)
fig_name = os.path.join(FIG_DIR, re.search("id=(.+jpg)&", fig_url).groups()[0])
if os.path.isfile(fig_name):
    print(f"{fig_name} exist!")
else:
    with open(fig_name, 'wb') as f_wb:
        f_wb.write(fig_html.content)

    print(f"{fig_name} success!")