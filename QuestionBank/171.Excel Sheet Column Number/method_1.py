#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-19 16:24
# @Author   : cancan
# @File     : method_1.py
# @Function : Excel表列序号


"""
Question:
给定一个Excel表格中的列名称，返回其相应的列序号。

Example，
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

Example 1:
输入: "A"
输出: 1

Example 2:
输入: "AB"
输出: 28

Example 3:
输入: "ZY"
输出: 701
"""

from string import ascii_uppercase


class Solution:
    def titleToNumber(self, s: str) -> int:
        d = {v: i + 1 for i, v in enumerate(ascii_uppercase)}

        r = 0

        for i, v in enumerate(s[::-1]):
            r += 26 ** i * d[v]

        return r
