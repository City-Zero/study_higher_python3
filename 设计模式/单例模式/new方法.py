import threading
'''
线程安全
'''
class New_Singleton():
    _instance = None

    def __new__(cls, *args, **kwargs):
        cls._instance = super(New_Singleton, cls).__new__(
            cls, *args, **kwargs) if not cls._instance else cls._instance
        return cls._instance
    def __init__(self):
        import time
        time.sleep(1)

def task():
    a = Singleton()
    print(a)


Singleton = New_Singleton
for i in range(10):
    threading.Thread(target=task).start()