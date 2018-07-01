#!/usr/bin/env python
# @Time     : 2018/7/1 下午6:39
# @Author   : cancan
# @File     : method_1.py
# @Function : 反转字符串中的单词 III

"""
Question:
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

Example:
输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc"

Note:
在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
"""


class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([i[::-1] for i in s.split(' ')])
