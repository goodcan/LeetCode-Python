#!/usr/bin/env python
# @Time     : 2018/7/15 下午1:39
# @Author   : cancan
# @File     : method_1.py
# @Function : 2的幂

"""
Question:
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

Example 1:
输入: 1
输出: true
解释: 20 = 1

Example 2:
输入: 16
输出: true
解释: 24 = 16

Example 3:
输入: 218
输出: false
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while True:
            if n == 1:
                return True
            if n % 2 == 0:
                n = n // 2
            else:
                return False
