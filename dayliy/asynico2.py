#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : asynico2.py
@version   : 1.0
@Time      : 2019/1/1 19:46
Description about this file: 

"""

import threading
import asyncio
import datetime


# @asyncio.coroutine
# def hello():
#     print('Hello world!(%s)'%threading.current_thread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)'%threading.current_thread())

async def hello():
    print('Hello world!(%s)' % threading.current_thread())
    r = await asyncio.sleep(1, result=datetime.datetime.now())

    print('Hello again! (%s) and there is result_%s' % (threading.current_thread(), r))


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
