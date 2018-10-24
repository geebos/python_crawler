#-*- coding: utf-8 -*
__author__ = 'geebos'
import threading


def print_hello_world():
    lock.acquire()
    print('Hello World')
    lock.release()

lock = threading.Lock()
threads = []
for i in range(10):
    t = threading.Thread(target=print_hello_world)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()