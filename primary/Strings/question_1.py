#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/5/3 9:58
# @Author   : cancan
# @File     : question_1.py
# @Function : 反转字符串

"""
Question:
请编写一个函数，其功能是将输入的字符串反转过来。

Example:
输入：s = "hello"
返回："olleh"
"""


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
