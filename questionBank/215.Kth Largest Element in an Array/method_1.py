#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/3 17:53
# @Author   : cancan
# @File     : method_1.py
# @Function : 数组中的第K个最大元素

"""
Question:
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

Example 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

Example 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

Note:
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums)[-k]
