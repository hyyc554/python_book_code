#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : 121.py.py
@version   : 1.0
@Time      : 2019/1/24 0:17
Description about this file: 

"""


class Solution:
    def maxProfit(self, prices):
        """
        这个需要注意的是，赋值一个0的最大利益，和一个无穷大的最小值
        遍历开始，比较当前价格与最小值的，取新的最小值赋值给最小价格
        当前利益等于当前价格减去历史最小值
        比较当前利益与历史最大利益，取最大赋值给最大利益
        :type prices: List[int]
        :rtype: int
        """

        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit
