#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : xx.py.py
@version   : 1.0
@Time      : 2019/1/20 21:42
Description about this file: 

"""
import importlib

path = "settings.Foo"
p, c = path.rsplit(".", maxsplit=1)
m = importlib.import_module(p)
cls = getattr(m, c)

print(m, cls)
# <module 'settings' from 'g:\\myflycode\\python_book_code\\dayliy\\flask\\import_with_str\\settings.py'> <class 'settings.Foo'>


print(dir(cls))
# ['DEBUG', 'TEST', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
for key in dir(cls):
    if key.isupper():
        print(key, getattr(cls, key))
# DEBUG True
# TEST True

