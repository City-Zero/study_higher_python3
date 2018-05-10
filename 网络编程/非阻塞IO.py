# coding=utf-8
import socket,fcntl,os

def recvall(sock,size):
    data = ''
    while len(data) < size:
        d = sock.recv(size-len(data))
        if not d:
            return None
        data += d
    return data

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.setblocking(False)
sock.f()
sock.bind(('127.0.0.1',12345))
sock.listen()
# fcntl.fcntl(sock,fcntl.F_SETFL,os.O_NONBLOCK)
while True:
    try:
        coon,addr = sock.accept()
        print(coon.recv(1024))
        coon.send('''HTTP/1.1 200 OK
    
        <html><head><title>hello</title></head></html>'''.encode('utf-8'))
        coon.close()
    except BlockingIOError:
        print('con')