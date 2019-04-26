#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/3/27 16:39
# @Author   : cancan
# @File     : method_2.py
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
        self.longest = ''

        queue = [(i, i) for i in range(len(s))]

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                queue.append((i, i + 1))

        while queue:
            self.go(s, queue)

        return self.longest

    def go(self, s, queue):

        i, j = queue.pop(0)

        if len(self.longest) < j - i + 1:
            self.longest = s[i:j + 1]

        if i - 1 >= 0 and j + 1 < len(s) and s[i - 1] == s[j + 1]:
            queue.append((i - 1, j + 1))
