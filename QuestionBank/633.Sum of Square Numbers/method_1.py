#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/10/14 14:15
# @Author   : cancan
# @File     : method_1.py
# @Function : 平方数之和

"""
给定一个非负整数你要判断是否存在两个整数 a 和 b，使得 + b2 = c 。

示例 1：
输入：c = 5
输出：true
解释：1 * 1 + 2 * 2 = 5

示例 2：
输入：c = 3
输出：false

提示：
0 <= c <= 231 - 1
"""

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = math.ceil(math.sqrt(c))
        while (i <= j):
            s = i ** 2 + j ** 2
            if s == c:
                return True
            if (s > c):
                j -= 1
            else:
                i += 1
        return False
