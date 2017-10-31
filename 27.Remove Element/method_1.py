#!/usr/bin/python
# -*- coding: utf-8 -*-

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
        while 1:
            try:
                nums.pop(nums.index(val))
            except:
                return len(nums)