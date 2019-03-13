#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-13 17:04
# @Author   : cancan
# @File     : method_2.py
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
        l = len(nums)

        dp = []

        dp.append([0] * l)  # 记录最大值
        dp.append([0] * l)  # 记录最小值

        dp[0][0] = nums[0]
        dp[1][0] = nums[0]

        for i in range(1, l):
            dp[0][i] = max(
                max(nums[i] * dp[0][i - 1], nums[i] * dp[1][i - 1]),
                nums[i]
            )

            dp[1][i] = min(
                min(nums[i] * dp[0][i - 1], nums[i] * dp[1][i - 1]),
                nums[i]
            )

        return max(dp[0][:])
