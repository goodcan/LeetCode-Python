#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/10 9:40
# @Author   : cancan
# @File     : question_5.py
# @Function : x 的平方根

"""
Question:
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

Example 1:
输入: 4
输出: 2

Example 2:
输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。
"""


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(x ** 0.5)
