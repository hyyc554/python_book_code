#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : 2.3.4.py
@version   : 1.0
@Time      : 2019/1/31 14:03
Description about this file:
2.3.4　具名元组
collections.namedtuple 是一个工厂函数，它可以用来构建一个带字段名的元组和一个有名字的类——这个带名字的类对调试程序有很大帮助。
1. 元组是一种很强大的可以当作记录来用的数据类型
2. 充当一个不可变的列表
"""

from collections import namedtuple

City = namedtuple("City", "name country population coordinates")
tokyo = City("Tokyo", "JP", 36.933, (35.689722, 139.691667))
print(tokyo)  # City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
print(type(tokyo))
print(City._fields) # ('name', 'country', 'population', 'coordinates')

LaLong = namedtuple("LatLong","lat long")
delhi_data = ("Delhi NCR","IN",21.935,LaLong(28.613889,77.208889))
delhi = City._make(delhi_data)
print(delhi._asdict())
print(delhi.coordinates.lat)


