#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : rabbit.py
@version   : 1.0
@Time      : 2019/2/1 20:31
Description about this file:

"""

import pika
conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel  = conn.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
conn.close()


