# coding=utf-8
'''
线程不安全
'''
class Singleton(object):
    _instance = None
    def __init__(self):
        import time
        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = Singleton(*args, **kwargs)
        return cls._instance

import threading

def task(arg):
    obj = Singleton.instance()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()

