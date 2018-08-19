#!/usr/bin/env python
# @Time     : 2018/7/1 下午10:01
# @Author   : cancan
# @File     : method_2.py
# @Function : 字符串中的单词数

"""
Question:
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
请注意，你可以假定字符串里不包括任何不可打印的字符。

Example:
输入: "Hello, my name is John"
输出: 5
"""


class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
