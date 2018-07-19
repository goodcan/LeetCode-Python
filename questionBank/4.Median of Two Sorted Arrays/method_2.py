#!/usr/bin/env python
# @Time     : 2018/7/19 下午10:50
# @Author   : cancan
# @File     : method_2.py
# @Function : 两个排序数组的中位数

"""
Question:
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。

Example 1:
nums1 = [1, 3]
nums2 = [2]
中位数是 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
中位数是 (2 + 3)/2 = 2.5
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        l = len(nums1)
        if l % 2 == 0:
            return (nums1[l // 2 - 1] + nums1[l // 2]) / 2
        else:
            return nums1[l // 2]
