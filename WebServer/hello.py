# coding=utf-8

# 函数式
def app(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    body = ''
    for i,j in environ.items():
        body += '<p>'+(str(i)+':::::'+str(j)+'<br><p>')
    return [body.encode('utf-8')]

# 实现__call__方法的类的实例变量
class app1:
    def __call__(self, environ,start_response):
        start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
        body = ''
        for i, j in environ.items():
            body += '<p>' + (str(i) + ':::::' + str(j) + '<br><p>')
        return [body.encode('utf-8')]


# 迭代法
class app2:
    def __init__(self,environ,start_response):
        self.environ = environ
        self.start_response = start_response

    def __iter__(self):
        self.start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
        body = ''
        for i, j in self.environ.items():
            body += '<p>' + (str(i) + ':::::' + str(j) + '<br><p>')
        yield body.encode('utf-8')