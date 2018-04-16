#!/usr/bin/env python
# @Time     : 2018/4/10 下午10:22
# @Author   : cancan
# @File     : method_1.py
# @Function : 买卖股票的最佳时机

"""
Question:
假设有一个数组，它的第 i 个元素是一个给定的股票在第 i 天的价格。
设计一个算法来找到最大的利润。你可以完成尽可能多的交易（多次买卖股票）。
然而，你不能同时参与多个交易（你必须在再次购买前出售股票）。
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        t = 0
        for i, v in enumerate(prices):
            next = i + 1
            if next < l and prices[next] > prices[i]:
                t += prices[next] - prices[i]

        return t
