#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Question:
给定一个整数数组，两个数字的返回索引，它们加到一个特定的目标。
您可能假设每个输入都有一个完全的解决方案，您可能不会重复使用相同的元素两次。

Example:
Given nums = [2, 7, 11, 15], target = 9
Because nums[0] + nums[1] = 2 + 7 = 9
return [0, 1]
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums_len_list = range(len(nums))
        for i in nums_len_list:
            n = target - nums[i]
            if (nums.count(n) != 0) and (nums.index(n) != i):
                return [i, nums.index(n)]
