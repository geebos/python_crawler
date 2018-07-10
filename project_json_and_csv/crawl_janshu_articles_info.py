#-*- coding: utf-8 -*
__author__ = 'geebos'
import requests
import csv
import json
from lxml import etree


#url生成器
def urlsGenerater(uid):
    # 设置请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
    }
    r = requests.get('https://www.jianshu.com/u/{}?order_by=shared_at&page={}'.format(uid, 1), headers=headers)
    dom = etree.HTML(r.text)

    #获取文章数量和最大页数
    article_num = int(dom.xpath('//div[@class="info"]//li[3]//p/text()')[0].strip())
    print(article_num)
    max_page_num = article_num / 9

    i = 1
    while True:
        yield 'https://www.jianshu.com/u/{}?order_by=shared_at&page={}'.format(uid, i)
        if i >= max_page_num:
            break
        i+=1

#获取文章的 xpath数组
def getArticleItems(url):
    #设置请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
    }
    # 获取所有 li标签
    xpath_items = '//ul[@class="note-list"]/li'

    r = requests.get(url, headers=headers)
    dom = etree.HTML(r.text)
    return dom.xpath(xpath_items)


#获取文章的相关信息
def getDetails(article_item):
    # 对每个 li标签再提取
    details_xpath = {
        'link': './div/a/@href',
        'title': './div/a/text()',
        'comment_num': './/div[@class="meta"]/a[2]/text()',
        'heart_num': './/div[@class="meta"]/span/text()',
    }

    items = details_xpath.items()
    detail = {}
    for key, path in items:
        detail[key] = ''.join(article_item.xpath(path)).strip()
    return detail

#通过 csv来保存数据 这里 csvobj要求是 csv.DictWriter
def csvSaveMethod(csvobj, data):
    csvobj.writerow(data)


#通过 json来保存数据 这里的 data必须是所有结果组成的一个列表
def jsonSaveMethod(data, fileobj):
    json.dump(data, fileobj, ensure_ascii=False, indent=2)

uid = '9bc194fde100'
urls = urlsGenerater(uid)

#保存 json结果的容器
results = []


#用 csvSaceMethod
with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['link', 'title', 'comment_num', 'heart_num']
    csvobj = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csvobj.writeheader()

    for url in urls:
        article_items = getArticleItems(url)
        for article_item in article_items:
            details = getDetails(article_item)
            #将结果添加到 results中，等下用 json写入
            results.append(details)
            csvSaveMethod(csvobj, details)

#用 jsonSaveMethod
with open('data.json', 'w', encoding='utf-8') as fp:
    jsonSaveMethod(results, fp)






