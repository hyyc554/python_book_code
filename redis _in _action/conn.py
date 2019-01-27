#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : conn.py
@version   : 1.0
@Time      : 2019/1/27 16:14
Description about this file: 

"""


import redis

pool = redis.ConnectionPool(host='127.0.0.1',password='hyc554')
r = redis.Redis(connection_pool=pool)


def main():
    print("ok")
    r.set('foo', 'bar1')

    print(r.get('foo').decode('utf8'))

if __name__ == '__main__':
    main()
