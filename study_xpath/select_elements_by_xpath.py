#-*- coding: utf-8 -*
__author__ = 'geebos'

#获取 id为 tab的 table标签下所有 tr标签
path = '//table[@id="tab"]//tr'
#和文件路径对比
path = 'D:\Github\hexo\source\_posts'

from lxml import etree
import requests

r = requests.get('http://www.baidu.com')

#作为示例的 html代码
html = '''<div class="container">
                <div class="row">
                    <div class="col">
                        <div class="card">
                            <div class="card-content">
                                <a href="#123333" class="box">
                                    点击我
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>'''

dom = etree.HTML(r.text)

#获取 a标签下的文本
a = dom.xpath('/')

print(a)