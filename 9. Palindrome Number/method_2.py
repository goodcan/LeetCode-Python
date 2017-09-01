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
        return str(x) == str(x)[::-1]