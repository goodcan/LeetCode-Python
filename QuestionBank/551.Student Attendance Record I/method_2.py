#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/10 12:11
# @Author   : cancan
# @File     : method_2.py
# @Function : 学生出勤纪录 I

"""
Question:
给定一个字符串来代表一个学生的出勤纪录，这个纪录仅包含以下三个字符：
'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果一个学生的出勤纪录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。
你需要根据这个学生的出勤纪录判断他是否会被奖赏。

Example 1:
输入: "PPALLP"
输出: True

Example 2:
输入: "PPALLL"
输出: False
"""


class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.count('A') <= 1 and s.count('LLL') == 0
