#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : args.py
@version   : 1.0
@Time      : 2019/6/16 10:34
Description about this file:

"""

def f(a, L=[]):
    L.append(a)
    return L

print(f(1),f.__defaults__) # [1] ([1],)

print(f(2),f.__defaults__) # [1, 2] ([1, 2],)
print(f(3),f.__defaults__) # [1, 2, 3] ([1, 2, 3],)
