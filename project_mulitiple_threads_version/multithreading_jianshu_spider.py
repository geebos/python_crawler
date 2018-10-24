#-*- coding: utf-8 -*
__author__ = 'geebos'
import threading
import queue
import jianshu_models



class UidGenerateThread(threading.Thread):
    def __init__(self, uid_queue):
        threading.Thread.__init__(self)
        self.uid_queue = uid_queue

    def run(self):
        start_users = [{'uid': 'a3ea268aeb60', 'follow_num': 525, 'fans_num': 2521, 'article_num': 118}]
        user_generator = jianshu_models.userUidsGenerator(start_users)
        while True:
            user = user_generator.__next__()
            self.uid_queue.put(user)


class DataCollectorThread(threading.Thread):
    def __init__(self, uid_queue, data_queue):
        threading.Thread.__init__(self)
        self.uid_queue = uid_queue
        self.data_queue = data_queue

    def run(self):
        while True:
            user = self.uid_queue.get()
            datas = jianshu_models.getArticleInfo(user)
            self.data_queue.put(datas)


class DataWriterThread(threading.Thread):
    def __init__(self, data_queue):
        threading.Thread.__init__(self)
        self.data_queue = data_queue
        self.writer = jianshu_models.simplifiedCsv(f'test/{self.name}.csv')

    def run(self):
        while True:
            data_list = self.data_queue.get()
            self.writer.writerows(data_list)




threads = []
uid_queue = queue.Queue(2000)
data_queue = queue.Queue(200)
t1 = UidGenerateThread(uid_queue)
threads.append(t1)

for i in range(15):
    t1 = DataWriterThread(data_queue)
    t2 = DataCollectorThread(uid_queue, data_queue)
    threads.append(t1)
    threads.append(t2)

for t in threads:
    t.start()

for t in threads:
    t.join()
