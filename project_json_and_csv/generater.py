#-*- coding: utf-8 -*
__author__ = 'geebos'


#url生成器
def urlsGenerater(uid):
    i = 1
    while True:
        yield 'https://www.jianshu.com/u/{}?order_by=shared_at&page={}'.format(uid, i)
        i+=1


uid = '9bc194fde100'
urls = urlsGenerater(uid)

for url in urls:
    print(url)