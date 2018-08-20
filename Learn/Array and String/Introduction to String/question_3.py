#!/usr/bin/env python
# @Time     : 2018/5/5 下午1:03
# @Author   : cancan
# @File     : question_3.py
# @Function : 最长公共前缀

"""
Question:
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

Example 1:
输入: ["flower","flow","flight"]
输出: "fl"

Example 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

Note:
所有输入只包含小写字母 a-z 。
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        t = min(strs, key=lambda x: len(x)) if strs else ''
        l = len(t)
        for i in strs:
            if t == i:
                continue
            for y in range(l):
                if t[:y + 1] != i[:y + 1]:
                    t = '' if y == 0 else t[:y]
                    break
        return t
