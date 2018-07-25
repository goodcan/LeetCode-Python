#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/25 15:19
# @Author   : cancan
# @File     : method_1.py
# @Function : 计数质数

"""
Question:
统计所有小于非负整数 n 的质数的数量。

Example:
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0

        if n < 3:
            return 0

        digits = [1] * n
        digits[0] = digits[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if digits[i] == 1:
                for j in range(i + i, n, i):
                    digits[j] = 0

        return sum(digits)
