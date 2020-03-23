# -*- coding: utf-8 -*-
"""
豆瓣电影排行榜

Created on Wed Aug 21 08:52:17 2019
"""
import os
import urllib
from bs4 import BeautifulSoup


file_dir, _ = os.path.split(os.path.realpath(__file__))
MOVIE_URL ='https://movie.douban.com/top250'
CSV_NAME = 'doubanmovie_top250.csv'
POSTER_DIR = os.path.join(file_dir, 'movie_posters')


def proxy_init():
    """代理配置"""
    proxy_support = urllib.request.ProxyHandler(
        {'http': 'http://user:password@proxycn2.huawei.com:8080',
         'https': 'http://user:password@proxycn2.huawei.com:8080'})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    

def html_get(url, decode="utf-8"):
    with urllib.request.urlopen(url) as response:
        html = response.read()
    if decode:
        html = html.decode(decode)
    return html
    
def html_parse(html_text):
    infos = []
    html_bs = BeautifulSoup(html_text, "html.parser")  # 创建BeautifulSoup对象
    block = html_bs.find('ol', {"class": "grid_view"})
    items = block.find_all('div', {'class': 'item'})
    for item in items:
        rank = item.find('em').string
        poster_url = item.find('img').attrs['src']
        titles = [t.string for t in item.find_all('span', {'class': 'title'})]
        details = [i.strip() for i in item.find('p').strings]
        star = [i.strip() for i in item.find('div', {"class": 'star'}).strings]
        star = [i for i in star if i]
        try:
            quote = item.find('span', {"class": 'inq'}).string
        except:
            quote = ''
        info = [rank, poster_url, quote] + titles + details + star
        infos.append(info)
    
    next_ = html_bs.find('span', {'class': 'next'})
    if next_:
        try:
            next_ = next_.find('link').attrs['href']
        except:
            next_ = None
    return infos, next_
    
def main():
    # proxy_init()
    
    info_lst = []
    url = MOVIE_URL
    while url:
        html_text = html_get(url)
        infos, next_ = html_parse(html_text)
        info_lst.extend(infos)
        if isinstance(next_,str):
            url = MOVIE_URL + next_
        else:
            url = None
            
    to_scv(info_lst)


def to_scv(info_lst):
    file_dir, _ = os.path.split(os.path.realpath(__file__))
    with open(os.path.join(file_dir, CSV_NAME), 'w', encoding='utf-8') as f:
        for info in info_lst:
            print(','.join(info), file=f)


def poster_saver(info_lst):
    if not os.path.isdir(POSTER_DIR):
        os.mkdir(POSTER_DIR)
    for info in info_lst:
        rank, poster_url, quote, title = info[:4]
        fig_name = f'{rank}_{title}.jpg'
        imgres = urllib.request.urlopen(poster_url).read()
        with open(os.path.join(POSTER_DIR, fig_name), "wb") as f: 
            f.write(imgres)

if __name__ == '__main__':
    main()
    