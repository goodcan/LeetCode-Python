#!/usr/bin/env python
# @Time     : 2018/5/5 上午11:11
# @Author   : cancan
# @File     : question_7.py
# @Function : 实现strStr()

"""
Question:
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

Example 1:
输入: haystack = "hello", needle = "ll"
输出: 2

Example 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1

Note:
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。
这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
"""


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            return haystack.index(needle)
        except ValueError:
            return -1
