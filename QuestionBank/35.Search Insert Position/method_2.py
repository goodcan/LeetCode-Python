#!/usr/bin/python

"""
Question:
给定一个排序数组和一个目标值，如果找到目标，返回索引。如果没有，则返回如果插入顺序的索引。

Example:
    [1,3,5,6], 5 → 2
    [1,3,5,6], 2 → 1
    [1,3,5,6], 7 → 4
    [1,3,5,6], 0 → 0
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l = len(nums)
        mid = l / 2
        low = 0
        high = l - 1
        while 1:
            if low > high:
                mid += 1
                break
            if target == nums[mid]:
                break
            elif target < nums[mid]:
                high = mid - 1
                mid = (low + high) / 2
            else:
                low = mid + 1
                mid = (low + high) / 2

        return mid
