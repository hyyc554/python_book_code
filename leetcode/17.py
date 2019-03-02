#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : 17.py.py
@version   : 1.0
@Time      : 2019/2/28 23:41
Description about this file:

"""

class Solution:
    def letterCombinations(self, digits):
        if '' == digits: return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return [lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, ['']]

a = Solution()

print(a.letterCombinations("23"))

