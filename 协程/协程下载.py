# coding=utf-8
import requests
import gevent
from gevent import monkey
import time

monkey.patch_all()

def Downloads(url):
    html = requests.get(url)
    f.write(html.text+'\n')

if __name__ == '__main__':
    num = 1000

    '''start_time = time.time()
    for _ in range(num):
        Downloads('http://www.baidu.com')
    print(time.time()-start_time)
    '''
    while True:
        f = open('proxy', 'a')
        start_time = time.time()
        gevent.joinall([gevent.spawn(Downloads,'http://flycold.cn:9010/get') for i in range(100)])
        print(time.time() - start_time)
        f.close()
