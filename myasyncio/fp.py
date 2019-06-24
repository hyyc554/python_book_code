#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : fp.py
@version   : 1.0
@Time      : 2019/4/11 23:05
Description about this file:

"""


# def frange(start, stop, increment):
#     x = start
#     while x < stop:
#         yield x
#         x += increment
# print(frange,type(frange(0,4,0.5)))
def countdown(n):
    print('开始计数', n)
    while n > 0:
        yield n
        n -= 1
    print('完成！')

c =countdown(3)
print(c)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
