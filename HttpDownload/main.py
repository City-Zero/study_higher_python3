# coding=utf-8
import socket
if __name__ == "__main__":
    sock = socket.socket()
    sock.connect(('www.baidu.com',80))
    sock.send('GET /img/bd_logo1.png HTTP/1.1\r\nHost:www.baidu.com\r\nUser-Agent: curl/7.59.0\r\nAccept: */*\r\nRange:bytes=-700\r\n\r\n'.encode())
    print(sock.recv(1024))