# -*- coding: utf-8 -*
__author__ = 'geebos'
import requests
from lxml import etree


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
}

# 获取所有 li标签
xpath_items = '//ul[@class="note-list"]/li'
# 对每个 li标签再提取
xpath_link = './div/a/@href'
xpath_title = './div/a/text()'
xpath_comment_num = './/div[@class="meta"]/a[2]/text()'
xpath_heart_num = './/div[@class="meta"]/span/text()'

urls = ['https://www.jianshu.com/u/9bc194fde100?order_by=shared_at&page='+str(i) for i in range(5)]
for url in urls:
    r = requests.get(url, headers=headers)
    dom = etree.HTML(r.text)
    items = dom.xpath(xpath_items)
    print(len(items))
    for t in items:
        print(t.xpath(xpath_title)[0])
