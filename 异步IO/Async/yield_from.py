# coding=utf-8
import socket
from selectors import DefaultSelector,EVENT_READ,EVENT_WRITE

epoller = DefaultSelector()
stopped = False
urls_todo = {'/'+str(i) for i in range(10)}

class Future:
    def __init__(self):
        self.result = None
        self._callbacks = []

    def add_done_callback(self,fn):
        self._callbacks.append(fn)

    def set_result(self,result):
        self.result = result
        for fn in self._callbacks:
            fn(self)

    # 改造为一个可迭代对象
    def __iter__(self):
        yield self
        return self.result

# 抽象sock连接功能
def connect(sock,address):
    f = Future()
    sock.setblocking(False)
    try:
        sock.connect(address)
    except BlockingIOError:
        pass

    def on_connected():
        f.set_result(None)
    epoller.register(sock.fileno(),EVENT_WRITE,on_connected)
    yield from f
    epoller.unregister(sock.fileno())

# 抽象单次recv()和读取完整的response功能
def read(sock):
    f = Future()

    def on_readable():
        f.set_result(sock.recv(4096))
    epoller.register(sock.fileno(),EVENT_READ,on_readable)
    chunk = yield from f
    epoller.unregister(sock.fileno())
    return chunk

def read_all(sock):
    response = []
    chunk = yield from read(sock)
    while chunk:
        response.append(chunk)
        chunk = yield from read(sock)
    return b''.join(response)

class Crawler:
    def __init__(self,url):
        self.url = url
        self.sock = None
        self.response = b''

    def fetch(self):
        global stopped
        sock = socket.socket()
        yield from connect(sock,('flycold.cn',80))
        get = 'GET {0} HTTP/1.0\r\nHost:flycold.cn\r\n\r\n'.format(self.url)
        sock.send(get.encode('utf-8'))
        self.response = yield from read_all(sock)
        urls_todo.remove(self.url)
        if not urls_todo:
            stopped = True

# 任务对象
class Task:
    def __init__(self,coro):
        self.coro = coro
        f = Future()
        f.set_result(None)
        self.step(f)

    def step(self,future):
        try:
            # send 会进入到coro执行，即fetch，直到下次yield
            # next_future 为yield返回的对象
            next_future = self.coro.send(future.result)
        except StopIteration:
            return
        next_future.add_done_callback(self.step)

def loop():
    while not stopped:
        # 阻塞，直到一个事件发生
        events = epoller.select()
        for fd,mask in events:
            callback = fd.data
            callback()

if __name__ == '__main__':
    import time
    start = time.time()
    for i in urls_todo:
        x = Crawler(i)
        Task(x.fetch())
    loop()
    print(time.time()-start)