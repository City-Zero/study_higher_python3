#coding=utf-8

def func0(lis = []):
    lis.append(1)
    print(lis)

def func1(*args):
    print(args)

def func2(**kwargs):
    print(kwargs)

def func3(app,ban):
    print(app,ban)

if __name__ == '__main__':
    func1(1,2,3,4,5)
    print('')
    func2(app=1,baa=2)
    print('')
    func0()
    func0()
    print('')
    args = (1,2)
    func3(*args)
    print('')
    kwargs={'app':1,'ban':2}
    func3(**kwargs)