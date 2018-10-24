#-*- coding: utf-8 -*
__author__ = 'geebos'
import threading
import requests
import time


# 定义一个子类并重载 __init__()方法和 run()方法
class testThread(threading.Thread):
    def __init__(self, url):
        # 初始化时调用基类的初始化函数 初始化基类
        threading.Thread.__init__(self)
        # 将参数赋值作为 self的属性 这样就可以将参数通过 self传递给 run方法
        self.url = url


    # 要在多线程里运行的函数
    def run(self):
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
        }
        for i in range(10):
            r = requests.get(self.url, headers=headers)
            print(r)


# 定义回调函数
def getPage(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
    }
    for i in range(10):
        r = requests.get(url, headers=headers)
        print(r)



url = 'https://www.jianshu.com/u/472a595d244c'

# 用来存放线程的列表
threads = []

# 记录开始时间
start = time.time()

# 添加十个线程到线程列表中
for i in range(10):
    ## 向线程列表传递参数，通过 kwargs向回调函数传递参数
    #t = threading.Thread(target=getPage, name=f'Thread {i}', kwargs={'url':url})
    ## 通过 args向回调函数传递参数, 注意 url后的逗号，
    ## args必须是一个元组
    ## t = threading.Thread(target=getPage, name=f'Thread {i}', args=(url,))
    t = testThread(url)
    threads.append(t)

# 开启所有线程
for t in threads:
    t.start()

# 阻塞主线程，直到所有线程全部完成
for t in threads:
    t.join()

# 记录结束时间
end = time.time()


#for i in range(10):
#    getPage(url)

end_1 = time.time()

print(f'多线程用时：{end - start}')
print(f'普通用时：{end_1 - end}')
