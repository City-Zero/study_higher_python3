# coding=utf-8

class A(object):
    #A.__doc__访问
    '学习类'

    #类变量，所有实例共用可用A.Count或A().Count
    #两个下划线，定义私有
    Count = 0

    #但可以通过A._A__all_Count / A()._A__all_Count访问
    __all_Count = 0

    #构造函数/初始方法,创建类的实例时自动调用本方法
    #self代表类的实例
    def __init__(self):
        A.__all_Count += 1
        A.Count += 1
        print('A__init__')

    def getAllCount(self):
        print(A.__all_Count)

    '''
    可通过setattr(类实例,'属性名','值')添加属性
    getattr(class,'name')
    hasattr(class,'name') ret:True/False
    delattr(class,'name') 删除属性
    __dict__ 返回属性字典
    '''

    #对象被销毁时调用
    def __del__(self):
        A.Count -= 1

class B(A):
    #子类会继承父类的类变量

    def __init__(self):
        print('B__init__')
        #如果子类定义有__init__，必须显示的调用父类的__init__
        A.__init__(self)

    def ChildMethod(self):
        print('子类方法')

class Par:
    def __new__(cls, *args, **kwargs):
        print('par new')
        #return object.__new__(cls,*args,**kwargs)

    def __init__(self):
        print("par init")

class Chi(Par):
    def __init__(self):
        print("chi init")