#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018-12-16 20:51
# @Author   : cancan
# @File     : method_1.py
# @Function : 字符串相乘

"""
Question:
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

Example 1:
输入: num1 = "2", num2 = "3"
输出: "6"

Example 2:
输入: num1 = "123", num2 = "456"
输出: "56088"

Note:
1.num1 和 num2 的长度小于110。
2.num1 和 num2 只包含数字 0-9。
3.num1 和 num2 均不以零开头，除非是数字 0 本身。
4.不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
"""


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) * int(num2))
