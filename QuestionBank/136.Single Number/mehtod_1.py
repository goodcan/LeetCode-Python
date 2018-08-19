#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/4/17 9:42
# @Author   : cancan
# @File     : method_1.py
# @Function : 只出现一次的数字

"""
Question:
给定一个整数数组，除了某个元素外其余元素均出现两次。请找出这个只出现一次的元素。

Note:
你的算法应该是一个线性时间复杂度。 你可以不用额外空间来实现它吗？
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        c = Counter(nums)
        return c.most_common()[-1][0]
