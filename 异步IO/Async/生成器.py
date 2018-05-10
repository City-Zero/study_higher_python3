# coding=utf-8

import socket
from selectors import DefaultSelector,EVENT_READ,EVENT_WRITE

epoller = DefaultSelector()
stopped = False
urls_todo = {'/'+str(i) for i in range(10)}

# 未来对象，result存放未来的执行结果
class Future:
    # 初始化结果和回调函数为空
    def __init__(self):
        self.result = None
        self._callbacks = []

    # 添加回调函数
    def add_done_callback(self,fn):
        self._callbacks.append(fn)

    # 设置结果并执行回调
    def set_result(self,result):
        self.result = result
        for fn in self._callbacks:
            fn(self)

# 爬虫类
class Crawler:
    def __init__(self,url):
        self.url = url
        self.sock = None
        self.response = b''

    def fetch(self):
        sock = socket.socket()
        sock.setblocking(False)
        try:
            sock.connect(('flycold.cn',80))
        except BlockingIOError:
            pass
        f = Future()

        def on_connected():
            f.set_result(None)

        epoller.register(sock.fileno(),EVENT_WRITE,on_connected)
        yield f
        epoller.unregister(sock.fileno())
        get = 'GET {0} HTTP/1.0\r\nHost:flycold.cn\r\n\r\n'.format(self.url)
        sock.send(get.encode('utf-8'))

        global stopped
        while True:
            f = Future()

            # sock可读时的事件
            def on_readable():
                f.set_result(sock.recv(4096))

            epoller.register(sock.fileno(),EVENT_READ,on_readable)
            chunk = yield f
            epoller.unregister(sock.fileno())
            if chunk:
                self.response += chunk
            else:
                urls_todo.remove(self.url)
                if not urls_todo:
                    stopped = True
                break

# 任务对象
class Task:
    # 初始化，设置爬虫任务对象，执行step
    def __init__(self,coro):
        self.coro = coro
        f = Future()
        f.set_result(None)
        self.step(f)

    # 单步执行
    def step(self,future):
        try:
            # send 会进入到coro执行，即fetch，直到下次yield
            # next_future 为yield返回的对象
            # 第一次发送None启动生成器，返回空的未来对象
            # 之后
            next_future = self.coro.send(future.result)
        except StopIteration:
            return
        # 新的未来对象添加回调
        next_future.add_done_callback(self.step)

def loop():
    while not stopped:
        # 阻塞，直到一个事件发生
        events = epoller.select()
        for fd,mask in events:
            # 收到的是send事件和recv事件
            callback = fd.data
            callback()

if __name__ == '__main__':
    import time
    start = time.time()

    # 循环创建爬虫任务
    for i in urls_todo:
        x = Crawler(i)
        # 启动爬虫协程，之后全部暂停在connect上
        Task(x.fetch())
    loop()
    print(time.time()-start)