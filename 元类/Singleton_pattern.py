# coding=utf-8
"""元类实现单例模式"""
import time,threading
class SingletonMetaclass(type):
    def __init__(self,*args,**kwargs):
        print('1.__init__')
        time.sleep(1)
        self.__instance = None
        super(SingletonMetaclass,self).__init__(*args,**kwargs)

    def __call__(self, *args, **kwargs):
        print('1.__call__')
        if self.__instance is None:
            self.__instance = super(SingletonMetaclass,self).__call__(*args,**kwargs)
        return self.__instance


class A(object,metaclass=SingletonMetaclass):
    def __init__(self,*args,**kwargs):
        pass

class SingletonMetaclass2(type):
    def __new__(cls,name,bases,attrs):
        print('2.__new__')
        attrs['_instance'] = None
        return super(SingletonMetaclass2,cls).__new__(cls,name,bases,attrs)

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        print('2.__call__')
        if self._instance is None:
            self._instance = super(SingletonMetaclass2,self).__call__(*args,**kwargs)
        return self._instance

class B(object,metaclass=SingletonMetaclass2):
    pass

"""
print(B._instance)
print(A._SingletonMetaclass__instance)
print(A() == A())
print(A.__dict__)
print(B.__dict__)
"""
for i in range(10):
    t = threading.Thread(target=lambda :print(A()),args=[])
    t.start()
