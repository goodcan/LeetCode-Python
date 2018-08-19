#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/1 14:49
# @Author   : cancan
# @File     : method_3.py
# @Function : 求众数

"""
Question:
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在众数。

Example 1:
输入: [3,2,3]
输出: 3

Example 2:
输入: [2,2,1,1,1,2,2]
输出: 2
"""


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        return Counter(nums).most_common()[0][0]

