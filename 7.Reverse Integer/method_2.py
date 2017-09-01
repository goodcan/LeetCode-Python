#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Question:
整数的反向数字。

Example1: x = 123, return 321
Example2: x = -123, return -321

Note:
输入假定为一个32位的带符号整数。
当反向的整数溢出时，函数应该返回0。
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
