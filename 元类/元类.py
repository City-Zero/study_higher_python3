# coding=utf-8

"""
普通类：
定义类，根据类的定义创建实例
元类：
定义元类，根据定义的元类创建类，再创建实例
"""

# metaclass是类的模板，所以必须从'type'类派生：
# 习惯上 元类的类名是以Metaclass结尾
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

class MyList(list,metaclass=ListMetaclass):
    pass
