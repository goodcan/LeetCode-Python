#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/20 10:59
# @Author   : cancan
# @File     : method_2.py
# @Function : 移除元素

"""
Question:
给定一个数组和一个值，删除该值的所有实例并返回新的长度。
不要为另一个数组分配额外的空间，您必须在固定内存的情况下这样做。
元素的顺序可以更改。不管你留了多少新长度。

Example:
给定一个数组和值 nums = [3,2,2,3], val = 3
您的函数应该返回length = 2，而nums的前两个元素为2。
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = len(nums)
        d = 0
        for i in range(l):
            if nums[i - d] == val:
                del nums[i - d]
                d += 1