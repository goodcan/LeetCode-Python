#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/21 11:01
# @Author   : cancan
# @File     : method_3.py
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
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        maxL = 0
        i = 0
        ret = ''
        while l - i > maxL / 2:
            left = i
            right = i
            while right + 1 < l and s[right + 1] == s[i]:
                right += 1
            i = right
            while left >= 0 and right < l and s[left] == s[right]:
                if right - left + 1 > maxL:
                    ret = s[left: right + 1]
                    maxL = right - left + 1
                left -= 1
                right += 1
            i += 1
        return ret
