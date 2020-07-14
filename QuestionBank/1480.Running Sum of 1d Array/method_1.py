#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/7/14 21:00
# @Author   : cancan
# @File     : method_.py
# @Function : 一维数组的动态和

"""
Question:
给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
请返回 nums 的动态和。

Example 1：
输入：nums = [1,2,3,4]
输出：[1,3,6,10]
解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。

Example 2：
输入：nums = [1,1,1,1,1]
输出：[1,2,3,4,5]
解释：动态和计算过程为 [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1] 。

Example 3：
输入：nums = [3,1,2,10,1]
输出：[3,4,6,16,17]

Note：
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        tmp = 0
        ans = []
        for v in nums:
            tmp += v
            ans.append(tmp)
        return ans
