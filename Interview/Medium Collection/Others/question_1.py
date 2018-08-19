#!/usr/bin/env python
# @Time     : 2018/6/30 下午2:54
# @Author   : cancan
# @File     : question_1.py
# @Function : 两整数之和

"""
Question:
不使用运算符 + 和-，计算两整数a 、b之和。

Example:
若 a = 1 ，b = 2，返回 3。
"""


class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum([a, b])
