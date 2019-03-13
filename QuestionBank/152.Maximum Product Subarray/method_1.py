#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-13 17:04
# @Author   : cancan
# @File     : method_1.py
# @Function : 乘积最大子序列

"""
Question：
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

Example 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

Example 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""


class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0

        res = nums[0]
        l = len(nums)

        for start in range(l):
            temp = nums[start]

            if temp > res:
                res = temp

            for end in range(start + 1, l):
                temp *= nums[end]

                if temp > res:
                    res = temp

        return res
