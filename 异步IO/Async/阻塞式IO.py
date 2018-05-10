# coding=utf-8
'''
阻塞式IO爬去10个页面
'''
import socket
urls_todo = {'/'+str(i) for i in range(10)}
host = 'www.baidu.com'

def fn(url):
    sock = socket.socket()
    sock.connect((host,80))
    sock.send('GET %s HTTP/1.0\r\n\r\n')