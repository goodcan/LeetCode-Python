#!/usr/bin/env python
# @Time     : 2018/7/1 下午12:05
# @Author   : cancan
# @File     : method_1.py
# @Function : 各位相加

"""
Question:
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

Example:
输入: 38
输出: 2
解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。

Follow up:
你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？
"""


class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return self.foo(num)

    def foo(self, num):
        if num < 10:
            return num
        else:
            s = str(num)
            return self.foo(sum([int(_) for _ in s]))
