# coding=utf-8

def outer(func):
    print('ahaha')
    def inner(msg):
        print('before do...')
        func(msg)
        print('after do...')
    return inner
print('1')
@outer
def do(msg):
    print('do %s...' % msg)
print('2')
def outer1(func):
    def inner():
        print('outer 1')
        func()
    return inner

def outer2(func):
    def inner():
        print('outer 2')
        func()
    return inner
@outer2
@outer1
def did():
    print('did something...')

msg = 'chicken'
for i in range(10):
    do(msg)

did()