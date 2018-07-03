#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/3 17:29
# @Author   : cancan
# @File     : method_1.py
# @Function : 两个数组的交集

"""
Question:
给定两个数组，写一个函数来计算它们的交集。

Example:
给定 num1= [1, 2, 2, 1], nums2 = [2, 2], 返回 [2].

Note:
1.每个在结果中的元素必定是唯一的。
2.我们可以不考虑输出结果的顺序
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))
