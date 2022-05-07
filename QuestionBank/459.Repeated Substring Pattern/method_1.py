#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/5/7 10:14
# @Author   : cancan
# @File     : method_1.py
# @Function : 重复的子字符串

"""
给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。

Example 1:
输入: s = "abab"
输出: true
解释: 可由子串 "ab" 重复两次构成。

Example 2:
输入: s = "aba"
输出: false

Example 3:
输入: s = "abcabcabcabc"
输出: true
解释: 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)
 
Note：
 - 1 <= s.length <= 104
 - s 由小写英文字母组成
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        d = 1
        while d <= l // 2:
            if l % d != 0:
                d += 1
                continue
            m = l // d if d != 1 else d
            tmp = s[:m]
            ok = True
            for idx in range(m, l, m):
                if s[idx:idx + m] != tmp:
                    ok = False
                    break
            if ok:
                return ok

            d += 1

        return False
