#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/5/4 9:53
# @Author   : cancan
# @File     : method_1.py
# @Function : 验证回文字符串

"""
Question:
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

Note:
本题中，我们将空字符串定义为有效的回文串。

Example 1:
输入: "A man, a plan, a canal: Panama"
输出: true

Example 2:
输入: "race a car"
输出: false
"""


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        s = ''.join(re.findall(r'(\w+|\d+)', s)).lower()
        return s == s[::-1]
