#!/usr/bin/env python
# @Time     : 2018/7/1 下午10:19
# @Author   : cancan
# @File     : method_1.py
# @Function : 最后一个单词的长度

"""
Question:
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
如果不存在最后一个单词，请返回 0 。

Note：
一个单词是指由字母组成，但不包含任何空格的字符串。

Example:
输入: "Hello World"
输出: 5
"""


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = s.split()
        return len(t[-1]) if t else 0
