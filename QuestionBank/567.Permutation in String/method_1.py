#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018-12-16 20:29
# @Author   : cancan
# @File     : method_1.py
# @Function : 字符串的排列

"""
Question:
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，第一个字符串的排列之一是第二个字符串的子串。

Example 1:
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").

Example 2:
输入: s1= "ab" s2 = "eidboaoo"
输出: False

Note:
1.输入的字符串只包含小写字母
2.两个字符串的长度都在 [1, 10,000] 之间
"""


class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s = {}

        for i in s1:
            if i in s:
                s[i] += 1
            else:
                s[i] = 1

        l1 = len(s1)
        l2 = len(s2)

        for i in range(l2 - l1 + 1):
            t = s2[i: i + l1]

            flag = True

            for j in s:
                if j not in t or t.count(j) != s[j]:
                    flag = False
                    break

            if flag:
                return True

        return False
