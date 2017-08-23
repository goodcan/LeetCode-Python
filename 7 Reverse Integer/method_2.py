#!/usr/bin/python
# -*- coding: utf-8 -*-

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
