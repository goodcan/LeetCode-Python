#!/usr/bin/env python
# @Time     : 2018/7/1 下午9:36
# @Author   : cancan
# @File     : method_1.py
# @Function : 单词模式

"""
Question:
给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。
这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串
str 中的每个非空单词之间存在着双向连接的对应模式。

Example 1:
输入: pattern = "abba", str = "dog cat cat dog"
输出: true

Example 2:
输入:pattern = "abba", str = "dog cat cat fish"
输出: false

Example 3:
输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false

Example 4:
输入: pattern = "abba", str = "dog dog dog dog"
输出: false

Note:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。
"""


class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        t = {}
        str_list = str.split()

        if len(pattern) != len(str_list):
            return False

        for p, s in zip(pattern, str_list):
            if t.get(p, None):
                if s != t[p]:
                    return False
            else:
                t[p] = s

        if len(set(t.keys())) != len(set(t.values())):
            return False

        return True
