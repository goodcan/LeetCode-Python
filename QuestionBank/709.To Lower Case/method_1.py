#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/31 13:41
# @Author   : cancan
# @File     : method_1.py
# @Function : 转换成小写字母

"""
Question:
实现函数 ToLowerCase()，该函数接收一个字符串参数 str，
并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。

Example 1：
输入: "Hello"
输出: "hello"

Example 2：
输入: "here"
输出: "here"

Example 3：
输入: "LOVELY"
输出: "lovely"
"""


class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()
