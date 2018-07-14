#!/usr/bin/env python
# @Time     : 2018/7/14 上午11:31
# @Author   : cancan
# @File     : method_1.py
# @Function : 二进制求和

"""
Question:
给定两个二进制字符串，返回他们的和（用二进制表示）。
输入为非空字符串且只包含数字 1 和 0。

Example 1:
输入: a = "11", b = "1"
输出: "100"

Example 2:
输入: a = "1010", b = "1011"
输出: "10101"
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]
