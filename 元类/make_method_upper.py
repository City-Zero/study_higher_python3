# coding=utf-8
"""
实现一个可以将类的属性都变成大写的元类
"""
# 用函数做元类
def UpperMethod(name,bases,attrs):
    new_attrs = dict()
    for k, v in attrs.items():
        if not k.startswith('_'):
            new_attrs[k.upper()] = v
        else:
            new_attrs[k] = v

    return type(name, bases, new_attrs)

# 用类做元类
class UpperMetaclass(type):
    def __new__(cls,name,bases,attrs):
        print('first in metaclass')
        print(attrs)
        new_attrs = dict()
        for k,v in attrs.items():
            if not k.startswith('_'):
                new_attrs[k.upper()] = v
            else:
                new_attrs[k] = v

        return type.__new__(cls,name,bases,new_attrs)

class Upper(object,metaclass=UpperMethod):
    num = 0
    def __init__(self,name,password):
        print('then in init')
        self.name = name
        self.password = password

print(dir(Upper))