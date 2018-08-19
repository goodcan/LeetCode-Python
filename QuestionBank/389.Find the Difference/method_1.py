#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/10 11:01
# @Author   : cancan
# @File     : method_1.py
# @Function : 找不同

"""
Question:
给定两个字符串 s 和 t，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。

Example:
输入：
s = "abcd"
t = "abcde"
输出：
e

Explanation:
'e' 是那个被添加的字母。
"""


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sd = {}
        td = {}

        def f(s, d):
            for i in s:
                if i not in d:
                    d[i] = 1
                else:
                    d[i] += 1

        f(s, sd)
        f(t, td)

        r = ''
        for i in td:
            if i not in sd:
                r += i * td[i]
            else:
                if td[i] > sd[i]:
                    r += i * (td[i] - sd[i])

        return r
