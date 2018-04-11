# coding=utf-8
import threading
'''
装饰器版本的单例模式
'''
def singleton(cls,*args,**kwargs):
    instances = dict()
    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
        return instances[cls]
    return getinstance

@singleton
class MyClass:
    def __init__(self):
        print('now time is')

for i in range(100):
    s = threading.Thread(target=lambda :print(id(MyClass())))
    s.start()
    #s.join()

