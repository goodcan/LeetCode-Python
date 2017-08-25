#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Note:
The input is assumed to be a 32-bit signed integer.
Your function should return 0 when the reversed integer overflows.
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # ` `类似repr()，repr()比str()对Python更友好

        s = cmp(x, 0)
        r = int(`s * x`[::-1])
        return s * r * (r <= (2 ** 31 - 1))
