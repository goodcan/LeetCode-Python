#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/9/19 21:05
# @Author   : cancan
# @File     : method_1.py
# @Function : 快乐数

"""
Question:
编写一个算法来判断一个数是不是“快乐数”。
一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

Example:
输入: 19
输出: true
解释:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        d = []

        while 1:
            d.append(n)
            n = str(n)
            t = 0
            for i in n:
                t += int(i) ** 2
            if t == 1:
                return True
            n = t
            if n in d:
                return False
