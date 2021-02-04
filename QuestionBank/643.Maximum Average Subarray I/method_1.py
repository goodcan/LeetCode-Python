#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2021/2/4 10:47
# @Author   : cancan
# @File     : method_1.py
# @Function : 子数组最大平均数 I

"""
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例：
输入：[1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75

提示：
- 1 <= k <= n <= 30,000。
- 所给数据范围 [-10,000，10,000]。
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tmp = ans = sum(nums[:k])
        for i in range(k, len(nums)):
            tmp = tmp - nums[i - k] + nums[i]
            if tmp > ans:
                ans = tmp
        return ans * 1.0 / k
