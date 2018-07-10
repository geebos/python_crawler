#-*- coding: utf-8 -*
__author__ = 'geebos'
import requests
from lxml import etree


#请求头和目标网址
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
}
url = 'https://www.jianshu.com/u/472a595d244c'

#第一种写法的 xpath
xpath_link = '//ul[@class="note-list"]/li/div/a/@href'
xpath_title = '//ul[@class="note-list"]/li/div/a/text()'
xpath_comment_num = '//ul[@class="note-list"]/li/div/div[@class="meta"]/a[2]/text()'
xpath_heart_num = '//ul[@class="note-list"]/li/div/div[@class="meta"]/span/text()'


#获取和解析网页
r = requests.get(url, headers=headers)
r.encoding = r.apparent_encoding
dom = etree.HTML(r.text)

#所有的 链接 标题 评论数 点赞数
links = dom.xpath(xpath_link)
titles = dom.xpath(xpath_title)
comment_nums = dom.xpath(xpath_comment_num)
heart_nums = dom.xpath(xpath_heart_num)

#将每篇文章的链接 标题 评论数 点赞数放到一个字典里
data = []
for i in range(len(links)):
    t = {}
    t['link'] = links[i]
    t['title'] = titles[i]
    t['comment_num'] = comment_nums[i].strip()
    t['heart_num'] = heart_nums[i].strip()
    data.append(t)

#打印结果
for t in data:
    print(t)


