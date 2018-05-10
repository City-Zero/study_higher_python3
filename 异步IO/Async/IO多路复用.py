import socket
from select import epoll,EPOLLIN,EPOLLOUT
import time

epoller = epoll()
stopped = False
urls_todo = {'/'+str(i) for i in range(10)}
fd_to_Crawler = {}

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
        fd_to_Crawler[self.sock.fileno()] = self
        epoller.register(self.sock.fileno(),EPOLLOUT)

    def connected(self):
        epoller.unregister(self.sock.fileno())
        get = 'GET {0} HTTP/1.0\r\nHost:flycold.cn\r\n\r\n'.format(self.url)
        self.sock.send(get.encode('utf-8'))
        epoller.register(self.sock.fileno(),EPOLLIN)

    def read_response(self):
        global stopped
        chunk = self.sock.recv(4096)
        if chunk:
            self.response += chunk
        else:
            epoller.unregister(self.sock.fileno())
            urls_todo.remove(self.url)
            if not urls_todo:
                stopped = True
        print(chunk.decode('utf-8'))

def loop():
    while not stopped:
        # 阻塞，直到一个事件发生
        events = epoller.poll()
        for fd,mask in events:
            if mask == EPOLLOUT:
                fd_to_Crawler[fd].connected()
            else:
                fd_to_Crawler[fd].read_response()

if __name__ == '__main__':
    start = time.time()
    for i in urls_todo:
        x = Crawler(i)
        x.fetch()
    loop()
    print(time.time()-start)