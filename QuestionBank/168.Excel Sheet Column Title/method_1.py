#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/3/19 16:08
# @Author   : cancan
# @File     : method_1.py
# @Function : Excel表列名称


"""
Question:
给定一个正整数，返回它在 Excel 表中相对应的列名称。

Exmpale，
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...

Example 1:
输入: 1
输出: "A"

Example 2:
输入: 28
输出: "AB"

Example 3:
输入: 701
输出: "ZY"
"""

from string import ascii_uppercase

class Solution:
    def convertToTitle(self, n: int) -> str:
        r = ''
        
        while n:
            n -= 1
            a, b = divmod(n, 26)
            r = ascii_uppercase[b] + r
            n = a
            
        return r
