#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Question:
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

        x = x
        if x >= 0:
            x = reversed(str(x))
            t = ''
            for i in x:
                t += i

            r = int(t)
            if r > (2 ** 31 - 1):
                return 0
            else:
                return r

        else:
            x = reversed(str(0 - x))
            t = ''
            for i in x:
                t += i

            r = int(t)
            if r > (2 ** 31 - 1):
                return 0
            else:
                return 0 - r