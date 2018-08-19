#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/30 18:53
# @Author   : cancan
# @File     : method_1.py
# @Function : 交替位二进制数

"""
Question:
给定一个正整数，检查他是否为交替位二进制数：换句话说，就是他的二进制数相邻的两个位数永不相等。

Example 1:
输入: 5
输出: True
解释:
5的二进制数是: 101

Example 2:
输入: 7
输出: False
解释:
7的二进制数是: 111

Example 3:
输入: 11
输出: False
解释:
11的二进制数是: 1011

Example 4:
输入: 10
输出: True
解释:
10的二进制数是: 1010
"""


class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b = bin(n)[2:]

        for i in range(len(b) - 1):
            if b[i] == b[i + 1]:
                return False

        return True
