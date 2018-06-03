# coding=utf-8
import selectors
import socket
import time

if __name__ == '__main__':
    l = []
    se = selectors.DefaultSelector()
    while True:
        x = input()
        if x == 'over':
            break
        else:
            l.append(x)
    for i in l:
        sock = socket.socket()
        sock.setblocking(False)
        try:
            sock.connect((i, 80))
        except BlockingIOError:
            # 非阻塞的异常
            pass
        se.register(sock,selectors.EVENT_WRITE,data=(time.time(),i))

    while l:
        event = se.select()
        for key,mask in event:
            if mask == selectors.EVENT_WRITE:
                print(key.data[1],time.time()-key.data[0])
                l.remove(key.data[1])
                se.unregister(key.fd)


