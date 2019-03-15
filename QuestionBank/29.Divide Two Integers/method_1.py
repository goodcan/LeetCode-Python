#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-15 17:54
# @Author   : cancan
# @File     : method_1.py
# @Function : 两数相除


"""
Question:
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。

Example 1:
输入: dividend = 10, divisor = 3
输出: 3

Example 2:
输入: dividend = 7, divisor = -3
输出: -2

Note:
1.被除数和除数均为 32 位有符号整数。
2.除数不为 0。
3.假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ma = 2 ** 31 - 1
        mi = -2 ** 31
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            r = divmod(dividend, divisor)[0]
        else:
            r = -divmod(abs(dividend), abs(divisor))[0]

        if r < mi:
            return mi
        elif r > ma:
            return ma
        else:
            return r
