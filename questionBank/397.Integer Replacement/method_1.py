#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/30 19:38
# @Author   : cancan
# @File     : method_1.py
# @Function : 整数替换

"""
Question:
给定一个正整数 n，你可以做如下操作：
    1. 如果 n 是偶数，则用 n / 2替换 n。
    2. 如果 n 是奇数，则可以用 n + 1或n - 1替换 n。
n 变为 1 所需的最小替换次数是多少？

Example 1:
输入: 8
输出: 3
解释: 8 -> 4 -> 2 -> 1

Example 2:
输入: 7
输出: 4
解释:
7 -> 8 -> 4 -> 2 -> 1
或
7 -> 6 -> 3 -> 2 -> 1
"""


class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """

        def f(n):
            if n < 3:
                return n - 1

            if n % 2 == 0:
                return f(n // 2) + 1
            else:
                return min(f(n - 1), f(n + 1)) + 1

        return f(n)
