#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/4/12 11:34
# @Author   : cancan
# @File     : method_1.py
# @Function : 反转字符串中的元音字母


"""
Question:
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

Example 1:
输入: "hello"
输出: "holle"

Example 2:
输入: "leetcode"
输出: "leotcede"

Note:
元音字母不包含字母"y"。
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        yy = {
            'a', 'e', 'i', 'o', 'u',
            'A', 'E', 'I', 'O', 'U'
        }

        s = list(s)

        r = 0
        l = len(s) - 1

        while l > r:
            if s[r] in yy and s[l] in yy:
                s[r], s[l] = s[l], s[r]
                r += 1
                l -= 1
            elif s[r] in yy and s[l] not in yy:
                l -= 1
            elif s[r] not in yy and s[l] in yy:
                r += 1
            else:
                r += 1
                l -= 1

        return ''.join(s)
