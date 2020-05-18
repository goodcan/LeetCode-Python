#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/19 00:13
# @Author   : cancan
# @File     : method_1.py
# @Function : 验证回   文字符串 Ⅱ


"""
Question:
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

Example 1:
输入: "aba"
输出: True

Exmaple 2:
输入: "abca"
输出: True
解释: 你可以删除c字符。

Note:
字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(low, high):
            while low < high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return check(low + 1, high) or check(low, high - 1)
        return True
