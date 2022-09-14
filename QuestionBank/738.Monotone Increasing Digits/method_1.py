#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/9/14 16:49
# @Author   : cancan
# @File     : method_1.py
# @Function : 单调递增的数字

"""
当且仅当每个相邻位数上的数字x和y满足x <= y时，我们称这个整数是单调递增的。
给定一个整数 n ，返回 小于或等于 n 的最大数字，且数字呈 单调递增 。

示例 1:
输入: n = 10
输出: 9

示例 2:
输入: n = 1234
输出: 1234

示例 3:
输入: n = 332
输出: 299

提示:
    0 <= n <= 109
"""
from typing import *

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = []
        for v in str(n):
            s.append(int(v))
        i = 1
        while i < len(s) and s[i] >= s[i-1]:
            i += 1
        if i < len(s):
            while i > 0 and s[i] < s[i-1]:
                s[i-1] -= 1
                i -= 1
            for j in range(i+1, len(s)):
                s[j] = 9
        ans = 0
        for v in s[::]:
            if v:
                ans *= 10
                ans += v
        return ans