#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/16 17:34
# @Author   : cancan
# @File     : method_1.py
# @Function : 第三大的数

"""
Question:
给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

Example 1:
输入: [3, 2, 1]
输出: 1
解释: 第三大的数是 1.

Example 2:
输入: [1, 2]
输出: 2
解释: 第三大的数不存在, 所以返回最大的数 2 .

Example 3:
输入: [2, 2, 3, 1]
输出: 1
解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
存在两个值为2的数，它们都排第二。
"""


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = list(set(nums))

        if len(nums) < 3:
            return max(nums)
        else:
            nums.sort()
            return nums[-3]