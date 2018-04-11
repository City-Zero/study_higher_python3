# coding=utf-8
"""
1.外函数中定义了内函数
2.内函数使用了外函数的变量
3.外函数的返回值是内函数的引用
一般来说，函数结束后，释放临时变量，但当外函数结束后，
会将内函数使用外函数的临时变量绑定给内函数

如何对闭包中内部函数调用外部函数的变量进行写操作（内函数中局部有效）？
1.该变量是可变的
2.该变量用nonlocal声明
"""
def outer():
    b = ['app']
    c = 20
    def inner():
        # nonlocal b
        print(locals())
        print(b)
        b.append('3')
        print(b)
    print(b)
    return inner

if __name__ == '__main__':
    demo = outer()
    demo()