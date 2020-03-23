# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 23:42:20 2019

@author: Sean
"""
import os
import urllib
from bs4 import BeautifulSoup


file_dir, _ = os.path.split(os.path.realpath(__file__))
ARTICLE_URL = r"https://kaoyan.wendu.com/2019/0708/138226.shtml#0-sqq-1-71196-9737f6f9e09dfaf5d3fd14d775bfee85"
ART_URL = "https://media.weibo.cn/article?id=2309404391865955778631"
HTML = r"""<div class="art-con-new"><p>仔细看哦~重点都在文中！</p><img src="https://wx3.sinaimg.cn/wap720/005YNKt6gy1g4snw71vzej30u016g4op.jpg" alt=""><img src="https://wx4.sinaimg.cn/wap720/005YNKt6gy1g4snw7lta0j30u016g4qp.jpg" alt=""><img src="https://wx1.sinaimg.cn/wap720/005YNKt6gy1g4snw8ayx0j30u016g4qp.jpg" alt=""><img src="https://wx2.sinaimg.cn/wap720/005YNKt6gy1g4snw8t4nzj30u016gh9k.jpg" alt=""><img src="https://wx3.sinaimg.cn/wap720/005YNKt6gy1g4snw9d6wcj30u016gnlk.jpg" alt=""><img src="https://wx1.sinaimg.cn/wap720/005YNKt6gy1g4snw9v9ctj30u016g1dr.jpg" alt=""><img src="https://wx4.sinaimg.cn/wap720/005YNKt6gy1g4snwafwmbj30u016gaz4.jpg" alt=""><img src="https://wx3.sinaimg.cn/wap720/005YNKt6gy1g4snwazpzuj30u016gayd.jpg" alt=""><img src="https://wx2.sinaimg.cn/wap720/005YNKt6gy1g4snwbijhqj30u016g4hr.jpg" alt=""><img src="https://wx2.sinaimg.cn/wap720/005YNKt6gy1g4sn0udlr5j30u016gnor.jpg" alt=""><img src="https://wx1.sinaimg.cn/wap720/005YNKt6gy1g4sn0v0s8ej30u016g4qp.jpg" alt=""><img src="https://wx2.sinaimg.cn/wap720/005YNKt6gy1g4sn0vpql6j30u016g1kx.jpg" alt=""><img src="https://wx2.sinaimg.cn/wap720/005YNKt6gy1g4sn0wd0dzj30u016g4qp.jpg" alt=""><img src="https://wx2.sinaimg.cn/wap720/005YNKt6gy1g4sn0wz4oyj30u016g1kx.jpg" alt=""><img src="https://wx2.sinaimg.cn/wap720/005YNKt6gy1g4sn0xivtlj30u016g4op.jpg" alt=""><img src="https://wx2.sinaimg.cn/wap720/005YNKt6gy1g4sn0y32s1j30u016g1kx.jpg" alt=""><img src="https://wx2.sinaimg.cn/wap720/005YNKt6gy1g4sn0ypqk6j30u016g4qp.jpg" alt=""><img src="https://wx3.sinaimg.cn/wap720/005YNKt6gy1g4sn0za1sxj30u016g1kx.jpg" alt=""><img src="https://wx1.sinaimg.cn/wap720/005YNKt6gy1g4sn0zwwg3j30u016g4qp.jpg" alt=""><img src="https://wx4.sinaimg.cn/wap720/005YNKt6gy1g4sn10i20qj30u016gnlr.jpg" alt=""><img src="https://wx2.sinaimg.cn/wap720/005YNKt6gy1g4sn114y9vj30u016g4qp.jpg" alt=""><img src="https://wx3.sinaimg.cn/wap720/005YNKt6gy1g4sn11wkuvj30u016g1kx.jpg" alt=""><img src="https://wx1.sinaimg.cn/wap720/005YNKt6gy1g4sn12ik8gj30u016g1kx.jpg" alt=""><img src="https://wx1.sinaimg.cn/wap720/005YNKt6gy1g4sn1373f1j30u016g1kx.jpg" alt=""><img src="https://wx2.sinaimg.cn/wap720/005YNKt6gy1g4sn13uijxj30u016g7vt.jpg" alt=""><img src="https://wx4.sinaimg.cn/wap720/005YNKt6gy1g4sn14fw0pj30u016g1it.jpg" alt=""><img src="https://wx2.sinaimg.cn/wap720/005YNKt6gy1g4sn1524ugj30u016g4qp.jpg" alt=""><img src="https://wx4.sinaimg.cn/wap720/005YNKt6gy1g4sn15mm3kj30u016g7pn.jpg" alt=""><img src="https://wx1.sinaimg.cn/wap720/005YNKt6gy1g4sn169ek1j30u016gb29.jpg" alt=""><img src="https://wx1.sinaimg.cn/wap720/005YNKt6gy1g4sn16r7c4j30u016gttg.jpg" alt=""><img src="https://wx1.sinaimg.cn/wap720/005YNKt6gy1g4sn17elebj30u016gnld.jpg" alt=""><img src="https://wx1.sinaimg.cn/wap720/005YNKt6gy1g4sn187d8ij30u016ge81.jpg" alt=""><img src="https://wx2.sinaimg.cn/wap720/005YNKt6gy1g4sn190eapj30u016ge81.jpg" alt=""><img src="https://wx4.sinaimg.cn/wap720/005YNKt6gy1g4sn19p43xj30u016ge81.jpg" alt=""><img src="https://wx3.sinaimg.cn/wap720/005YNKt6gy1g4sn1abbuzj30u016ge1f.jpg" alt=""><img src="https://wx4.sinaimg.cn/wap720/005YNKt6gy1g4sn1arpamj30u016gtst.jpg" alt=""><img src="https://wx2.sinaimg.cn/wap720/005YNKt6gy1g4sn1b816wj30u016gdtq.jpg" alt=""><img src="https://wx2.sinaimg.cn/wap720/005YNKt6gy1g4sn1bp1s6j30u016gwx1.jpg" alt=""><img src="https://wx1.sinaimg.cn/wap720/005YNKt6gy1g4sn1c4vowj30u016gwya.jpg" alt=""><img src="https://wx1.sinaimg.cn/wap720/005YNKt6gy1g4sn1cmdecj30u016g1ai.jpg" alt=""><img src="https://wx3.sinaimg.cn/wap720/005YNKt6gy1g4sn1d4kh1j30u016gaw3.jpg" alt="">​​​</div>"""
FIG_DIR = POSTER_DIR = os.path.join(file_dir, 'figs')

def html_get(url, decode="utf-8"):
    
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
    except :
        print ("URLError")
        return
    if decode:
        html = html.decode(decode)
    return html


def html_parse(html_text):
    html_bs = BeautifulSoup(html_text, "html.parser")
    imgs = html_bs.find_all('img')
    img_urls = [img.attrs['src'] for img in imgs]
    return img_urls


def fig_dl(img_urls):
    if not os.path.isdir(FIG_DIR):
        os.mkdir(FIG_DIR)
        
    for i, f_url in enumerate(img_urls):
        fig_name = f'{i:0>3d}.jpg'
        imgres = urllib.request.urlopen(f_url).read()
        with open(os.path.join(FIG_DIR, fig_name), "wb") as f: 
            f.write(imgres)
    

def main():
#    html = html_get(ARTICLE_URL)
    html_text = HTML
    img_urls = html_parse(html_text)
    fig_dl(img_urls)
    
    
if __name__ == "__main__":
    main()
    pass
