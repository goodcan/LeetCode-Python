#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Question:
Given an array of integers, return indices of the two
numbers such that they add up to a specific target.
You may assume that each input would have exactly one
solution, and you may not use the same element twice.

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
