#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/5/3 10:07
# @Author   : cancan
# @File     : method_3.py
# @Function : 颠倒整数

"""
Question:
给定一个 32 位有符号整数，将整数中的数字进行反转。

Example 1:
输入: 123
输出: 321

Example 2:
输入: -123
输出: -321

Example 3:
输入: 120
输出: 21

Note:
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。
根据这个假设，如果反转后的整数溢出，则返回 0。
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        f = lambda x: x if -2 ** 31 <= x <= 2 ** 31 - 1 else 0
        if x > 0:
            return f(int(str(x)[::-1]))
        elif x < 0:
            return f(int('-' + str(x)[1:][::-1]))
        else:
            return x
