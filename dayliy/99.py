#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : 99.py
@version   : 1.0
@Time      : 2019/1/31 20:59
Description about this file:

"""

print('\n'.join(['\t'.join(["%2s*%2s=%2s" % (j, i, i * j) for j in range(1, i + 1)]) for i in range(1, 10)]))
