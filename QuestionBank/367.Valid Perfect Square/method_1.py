#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/5/7 10:27
# @Author   : cancan
# @File     : method_1.py
# @Function : 有效的完全平方数

"""
给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
进阶：不要 使用任何内置的库函数，如  sqrt 。

Example 1：
输入：num = 16
输出：true

Example 2：
输入：num = 14
输出：false

Note：
 -1 <= num <= 2^31 - 1
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 1

        while start <= num:
            tmp = start ** 2
            if tmp == num:
                return True
            if tmp > num:
                return False
            start += 1

        return False
