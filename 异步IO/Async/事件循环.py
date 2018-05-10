# coding=utf-8
import socket
from selectors import DefaultSelector,EVENT_READ,EVENT_WRITE
import time

'''
相比于select模块，官方更推荐使用selectors这个高级IO多路复用库
'''

# 自动选择最高效的IO多路复用，Linux上默认是epoll
selector = DefaultSelector()
stopped = False
urls_todo = {'/'+str(i) for i in range(10)}

class Crawler:
    def __init__(self,url):
        self.url = url
        self.sock = None
        self.response = b''

    def fetch(self):
        self.sock = socket.socket()
        self.sock.setblocking(False)
        try:
            self.sock.connect(('flycold.cn',80))
        except BlockingIOError:
            pass
        # 注册sock的可写事件（connect完成时）
        selector.register(self.sock.fileno(),EVENT_WRITE,self.connected)

    # 当connect完成时发request
    def connected(self,key,mask):
        # 取消注册
        selector.unregister(key.fd)
        get = 'GET {0} HTTP/1.0\r\nHost:flycold.cn\r\n\r\n'.format(self.url)
        self.sock.send(get.encode('utf-8'))
        # 注册可读事件（当服务器给予回应时）
        selector.register(key.fd,EVENT_READ,self.read_response)

    # 当服务器回应后触发
    def read_response(self,key,mask):
        global stopped
        chunk = self.sock.recv(4096)
        if chunk:
            self.response += chunk
        else:
            selector.unregister(key.fd)
            urls_todo.remove(self.url)
            self.sock.close()
            if not urls_todo:
                stopped = True
        print(chunk.decode('utf-8'))

# 事件循环 注册事件后，需要获取哪个套接字触发了事件，并去处理
def loop():
    while not stopped:
        # 阻塞，直到一个事件发生
        events = selector.select()
        for event_key,event_mask in events:
            callback = event_key.data
            callback(event_key,event_mask)

if __name__ == '__main__':
    start = time.time()
    for i in urls_todo:
        x = Crawler(i)
        x.fetch()
    loop()
    print(time.time()-start)