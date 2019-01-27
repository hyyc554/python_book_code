#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : 5.3.py
@version   : 1.0
@Time      : 2019/1/27 16:01
Description about this file: 

"""
# from python_book_code.redis_in_action.conn import r
# from python_book_code. import r
import time
import redis

pool = redis.ConnectionPool(host='127.0.0.1', password='hyc554')
r = redis.Redis(connection_pool=pool)
# print(r.get('foo').decode('utf8'))
PRECISION = [1, 5, 60, 300, 3600, 18000, 86400]


# r.zadd("known:", "hash", 0)
# r.zadd(name="known:",mapping={"hash":0})

def update_counter(conn, name, count=1, now=None):
    now = now or time.time()
    pipe = conn.pipeline()
    for prec in PRECISION:
        pnow = int(now / prec) * prec
        hash = "%s:%s" % (prec, name)
        pipe.zadd("known:", mapping={hash: 0})
        pipe.hincrby("count:" + hash, pnow, count)
    pipe.execute()


def get_counter(conn, name, precision):
    hash = "%s:%s" % (precision, name)
    data = conn.hgetall("count:" + hash)
    to_return = []
    for key, value in data.items():
        to_return.append((int(key), int(value)))
        to_return.sort()
    return to_return


def main():
    update_counter(conn=r, name="hyc")
    res = get_counter(conn=r, name="hyc", precision=300)
    print(res)


if __name__ == '__main__':
    main()
