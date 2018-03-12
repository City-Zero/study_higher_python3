#coding=utf-8
import time

def print_args(func):
    def inner(*args,**kwargs):
        print('%s,%s'%(args,kwargs))
        return func(*args,**kwargs)
    return inner

def print_logger(func):
    def inner():
        print('singal logger!')
        return func()
    return inner

@print_logger
def st():
    print(1)

@print_args
def bar(*args,**kwargs):
    print('do something...')


if __name__ == '__main__':
    bar(1,23,3,app='ewe',str='zxs')
    st()