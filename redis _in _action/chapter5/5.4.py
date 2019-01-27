#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : 5.4.py
@version   : 1.0
@Time      : 2019/1/27 17:48
Description about this file: 

"""
from conn import r

def get_counter(conn, name, precision):
    hash = "%s:%s" % (precision, name)
    data = conn.hgetall("count:" + hash)
    to_return = []
    for key, value in data.items():
        to_return.append((int(key), int(value)))
        to_return.sort()
    return to_return

def main():
    r.hgetall("hyc")

if __name__ == '__main__':
    main()