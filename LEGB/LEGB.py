# coding=utf-8
"""Python变名命名空间以及LEGB规则"""
"""
LEGB含义解释：
L-Local(function)；函数内的名字空间
E-Enclosing function locals；外部嵌套函数的名字空间(例如closure)
G-Global(module)；函数定义所在模块（文件）的名字空间
B-Builtin(Python)；Python内置模块的名字空间
"""
a = 1
b = 'G'
def foo():
    a = 2
    b = 'foo'
    def foo1():
        a = 3
        def foo2():
            a = 4
            b = 'foo2'
            print("foo2",a)
            def foo4():
                print("foo4",b)
            foo4()
        print("foo1",a)
        foo2()
    foo1()
    print("foo",a)

foo()