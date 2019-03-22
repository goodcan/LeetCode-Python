#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-22 10:41
# @Author   : cancan
# @File     : method_1.py
# @Function : 字符的最短距离


"""
Question:
给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。

Example 1:
输入: S = "loveleetcode", C = 'e'
输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

Note:
字符串 S 的长度范围为 [1, 10000]。
C 是一个单字符，且保证是字符串 S 里的字符。
S 和 C 中的所有字母均为小写字母。
"""


class Solution:
    def shortestToChar(self, S, C):
        ans = []
        s = -1
        n = 0

        for i, v in enumerate(S):

            if v != C:
                n += 1
            else:

                if s == -1:
                    ans = [j for j in range(i + 1)][::-1]
                else:
                    d = i - s - 1
                    t = [j for j in range(d // 2 + 1)]

                    if d % 2 == 0:
                        ans = ans[:-1] + t + t[::-1]
                    else:
                        ans = ans[:-1] + t + [d // 2 + 1] + t[::-1]
                s = i
                n = 0

        if n != 0:
            ans = ans[:-1] + [j for j in range(n + 1)]

        return ans
