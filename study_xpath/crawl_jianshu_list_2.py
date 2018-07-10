#-*- coding: utf-8 -*
__author__ = 'geebos'
import requests
from lxml import etree


#请求头和目标网址
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
}
url = 'https://www.jianshu.com/u/472a595d244c'

#第二种写法的 xpath
#获取所有 li标签
xpath_items = '//ul[@class="note-list"]/li'
#对每个 li标签再提取
xpath_link = './div/a/@href'
xpath_title = './div/a/text()'
xpath_comment_num = './/div[@class="meta"]/a[2]/text()'
xpath_heart_num = './/div[@class="meta"]/span/text()'


#获取和解析网页
r = requests.get(url, headers=headers)
r.encoding = r.apparent_encoding
dom = etree.HTML(r.text)

#获取所有的文章标签
items = dom.xpath(xpath_items)

#分别对每一个文章标签进行操作 将每篇文章的链接 标题 评论数 点赞数放到一个字典里
data = []
for article in items:
    t = {}
    t['link'] = article.xpath(xpath_link)[0]
    t['title'] = article.xpath(xpath_title)[0]
    #comment_num对应的标签里有两个文本标签 用 join方法将两个文本拼接起来
    #strip()方法去除换行和空格
    t['comment_num'] = ''.join(article.xpath(xpath_comment_num)).strip()
    t['heart_num'] = article.xpath(xpath_heart_num)[0].strip()
    data.append(t)

#打印结果
for t in data:
    print(t)


