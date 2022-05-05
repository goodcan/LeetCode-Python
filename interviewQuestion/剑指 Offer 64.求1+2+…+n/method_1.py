#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/6/2 11:39
# @Author   : cancan
# @File     : method_1.py
# @Function : 求1+2+…+n

"""
Question:
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

Example 1：
输入: n = 3
输出: 6

Example 2：
输入: n = 9
输出: 45

Note：
1 <= n <= 10000
"""

class Solution:
    def sumNums(self, n: int) -> int:
        return int((1 + n) * n / 2)

