#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/24 14:58
# @Author   : cancan
# @File     : question_5.py
# @Function : 最大连续1的个数

"""
Question:
给定一个二进制数组， 计算其中最大连续1的个数。

Example 1:
输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.

Note
1.输入的数组只包含 0 和1。
2.输入数组的长度是正整数，且不超过 10,000。
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = {1: 0}
        r = t[1]

        for i, v in enumerate(nums):
            if v == 1:
                t[v] += 1
            else:
                if t[1] > r:
                    r = t[1]
                t[1] = 0

        return t[1] if t[1] > r else r
