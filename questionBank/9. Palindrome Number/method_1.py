#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Question:
确定一个整数是否为回文。
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = 0 - x

        if a < 0:
            q = str(x)
        elif a == 0:
            return True
        else:
            return False

        if len(str(x)) == 1:
            return True

        l = len(q) / 2

        if q[:l] == q[(0 - l):][::-1]:
            return True
        else:
            return False