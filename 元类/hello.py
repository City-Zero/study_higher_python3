# coding=utf-8
"""
直接定义类与动态使用type函数生成类
"""

# 直接定义
class Helloa(object):
    'Hello'
    times = 0
    def hello(self,name='world'):
        print('Hello,%s.' % name)
        self.times += 1

# type
def fn(self,name='world'):
    print('Hello,%s.' % name)
    self.times += 1

Hello = type('Hello',(object,),dict(times=0,hello = fn))
a = Hello()
a.hello()
print(a.times)
print(type(Hello))
print(type(a))