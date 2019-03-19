#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-19 16:57
# @Author   : cancan
# @File     : method_1.py
# @Function : 存在重复元素 II


"""
Question:
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

Example 1:
输入: nums = [1,2,3,1], k = 3
输出: true

Example 2:
输入: nums = [1,0,1,1], k = 1
输出: true

Example 3:
输入: nums = [1,2,3,1,2,3], k = 2
输出: false
"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        t = {}

        for i, v in enumerate(nums):
            if v in t:
                if i - t[v] <= k:
                    return True
                else:
                    t[v] = i
            else:
                t[v] = i

        return False
