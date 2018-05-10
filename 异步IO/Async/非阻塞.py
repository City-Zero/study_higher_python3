import socket
import time
def nonblocking_way():
    sock = socket.socket()
    sock.setblocking(False)
    try:
        sock.connect(('www.baidu.com',80))
    except BlockingIOError:
        # 非阻塞的异常
        pass
    request = 'GET / HTTP/1.0\r\nHost:www.baidu.com\r\n\r\n'
    data = request.encode('utf-8')
    # 不知sock何时就绪，所以不断尝试发送
    while True:
        try:
            sock.send(data)
            # 直到不异常，才发送完成
            break
        except OSError:
            pass

    response = b''
    while True:
        try:
            chunk = sock.recv(4096)
            while chunk:
                response += chunk
                # blocking
                chunk = sock.recv(4096)
            break
        except OSError:
            pass
    return response

def sync_way():
    res = []
    for i in range(10):
        res.append(nonblocking_way())
    return len(res)

if __name__ == '__main__':
    start = time.time()
    print(sync_way())
    print(time.time()-start)