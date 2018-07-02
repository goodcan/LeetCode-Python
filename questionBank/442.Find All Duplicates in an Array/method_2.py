#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/2 19:44
# @Author   : cancan
# @File     : method_2.py
# @Function : 数组中重复的数据

"""
Question:
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
找到所有出现两次的元素。
你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？

Example:
输入: [4,3,2,7,8,2,3,1]
输出: [2,3]
"""


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter

        c = Counter(nums)
        res = []
        for k, v in c.items():
            if v > 1:
                res.append(k)
        return res
