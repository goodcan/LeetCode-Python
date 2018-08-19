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

from bisect import bisect_left


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 第一个参数必须是排序后的列表
        return bisect_left(nums, target)