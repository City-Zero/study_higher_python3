# coding=utf-8

from wsgiref.simple_server import make_server
from hello import app2

# 创建一个服务器，第三个参数是处理函数
httpd = make_server('0.0.0.0',8000,app2)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求
httpd.serve_forever()