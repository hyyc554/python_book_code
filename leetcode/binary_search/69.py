#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : 69.py
@version   : 1.0
@Time      : 2019/4/8 21:17
Description about this file:

"""


class Solution:
    def mySqrt(self, x):
        l = 1
        r = x
        while l <= r:
            m = (r + l) // 2
            if m * m > x:
                r = m - 1
            else:
                l = m + 1
        return r


class Solution:
    def mySqrt(self, x):
        if x <= 1:
            return x
        s = 1
        while True:
            if s * s > x:
                return s - 1
            s += 1


class Solution:
    def mySqrt(self, x):
        a= x
        while a * a > x:
            a = (a + x // a) // 2
        return a


a = Solution()
print(a.mySqrt(14324324234234234234234235423532453252))
