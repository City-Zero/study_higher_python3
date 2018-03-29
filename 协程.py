# coding=utf-8


def func1(n):
    for i in range(n):
        print('func1:before yield,i=%d' % i)
        x = yield
        print('func1:after yield,i=%d,x=%s' % (i,x))


def func2(n):
    for i in range(n):
        print('func2:before yield,i=%d' % i)
        x = yield
        print('func2:after yield,i=%d,x=%s' % (i,x))

if __name__ == '__main__':
    a = func1(5)
    b = func2(5)

    next(a)
    a.send(1)
    a.send(None)
    next(b)
    a.send(2)
    b.send(3)