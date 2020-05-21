#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/3/27 16:39
# @Author   : cancan
# @File     : method_1.py
# @Function : 最长回文子串


"""
Question:
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

Example 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

Example 2：
输入: "cbbd"
输出: "bb"
"""


class Solution:
    def longestPalindrome(self, s):

        if not s:
            return s

        l = len(s)
        end = l // 2

        for j in range(end, 0, -1):
            ans = None
            for start in range(l - j):
                if s[start:start + j] == s[start + j + 1:start + 2 * j + 1][::-1]:
                    return s[start:start + 2 * j + 1]
                elif s[start:start + j] == s[start + j:start + 2 * j][::-1]:
                    ans = s[start:start + 2 * j]

            if ans:
                return ans

        return s[0]
