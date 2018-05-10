import socket
import time
def blocking_way():
    sock = socket.socket()
    # blocking
    sock.connect(('www.baidu.com',80))
    request = 'GET / HTTP/1.0\r\nHost:www.baidu.com\r\n\r\n'
    sock.send(request.encode('utf-8'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        # blocking
        chunk = sock.recv(4096)
    return response

def sync_way():
    res = []
    for i in range(10):
        res.append(blocking_way())
    return len(res)

if __name__ == '__main__':
    start = time.time()
    print(sync_way())
    print(time.time()-start)