#coding=utf-8
class Conf():
    _instance = None
    def __new__(cls, *args, **kwargs):
        cls._instance = super(Conf,cls).__new__(cls,*args,**kwargs) if not cls._instance else cls._instance
        return cls._instance

a = Conf()
b = Conf()
print(id(a))
print(id(b))
