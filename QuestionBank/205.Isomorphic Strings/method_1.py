#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-19 16:45
# @Author   : cancan
# @File     : method_1.py
# @Function : 同构字符串


"""
Question:
给定两个字符串 s 和 t，判断它们是否是同构的。
如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

Example 1:
输入: s = "egg", t = "add"
输出: true

Example 2:
输入: s = "foo", t = "bar"
输出: false

Example 3:
输入: s = "paper", t = "title"
输出: true

Note:
你可以假设 s 和 t 具有相同的长度。
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        for i, v in enumerate(s):
            if s.index(v) != t.index(t[i]):
                return False

        return True
