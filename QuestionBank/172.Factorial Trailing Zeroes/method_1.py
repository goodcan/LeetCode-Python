#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-05 22:05
# @Author   : cancan
# @File     : method_1.py
# @Function : 阶乘后的零

"""
Question:
给定一个整数 n，返回 n! 结果尾数中零的数量。

Example 1:
输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。

Example 2:
输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.

Note:
你算法的时间复杂度应为 O(log n) 。
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        total = 0
        while n > 4:
            n //= 5
            total += n
        return total
