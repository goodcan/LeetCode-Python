#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-01 16:13
# @Author   : cancan
# @File     : method_1.py
# @Function : 分割回文串


"""
Question:
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。

Example:
输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
"""


class Solution:
    def partition(self, s):
        res = []
        temp = []
        self.do(res, temp, s, 0)
        return res

    def do(self, res, temp, s, start):
        """执行分割"""

        if start == len(s):
            res.append(temp.copy())
            return

        # 动态规划
        for i in range(start, len(s)):
            st = s[start:i + 1]
            if self.isPalindrome(st):
                print(st)
                temp.append(st)
                self.do(res, temp, s, i + 1)
                temp.pop()

    def isPalindrome(self, s):
        """判断是否是回文"""

        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True
