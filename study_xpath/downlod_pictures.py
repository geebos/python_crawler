#-*- coding: utf-8 -*
__author__ = 'geebos'

import requests
from lxml import etree


#网站地址
url = 'http://www.netbian.com/'

#获取网页
r = requests.get(url)
r.encoding = r.apparent_encoding
#解析网页
dom = etree.HTML(r.text)

#获取图片 img标签
#先获取图片所在的 img标签在分别获取图片链接和名字
img_path = '//a[@title]/img'
imgs = dom.xpath(img_path)

#获取图片的链接和名字 并下载 命名 保存
for img in imgs:
    #xpath 的相对路径 “.” 代表上一级标签
    #不要忘记 xpath返回的总是列表！
    src = img.xpath('./@src')[0]
    name = img.xpath('./@alt')[0]

    #下载图片
    image = requests.get(src)
    #命名并保存图片
    with open(name+'.jpg', 'wb') as f:
        f.write(image.content)