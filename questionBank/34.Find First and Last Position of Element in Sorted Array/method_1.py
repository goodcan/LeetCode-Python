#!/usr/bin/env python
# @Time     : 2018/7/21 下午5:43
# @Author   : cancan
# @File     : method_1.py
# @Function : 在排序数组中查找元素的第一个和最后一个位置

"""
Question:
给定一个按照升序排列的整数数组 nums，和一个目标值 target。
找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。

Example 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

Example 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1, -1]

        start = nums.index(target)
        end = start + 1
        l = len(nums)

        while end < l and nums[end] == target:
            end += 1

        end -= 1

        return [start, end]
