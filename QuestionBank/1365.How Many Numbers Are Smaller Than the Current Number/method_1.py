#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/5 14:44
# @Author   : cancan
# @File     : method_1.py
# @Function : 有多少小于当前数字的数字

"""
Question:
给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。
换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。
以数组形式返回答案。

Example 1：
输入：nums = [8,1,2,2,3]
输出：[4,0,1,1,3]
解释：
对于 nums[0]=8 存在四个比它小的数字：（1，2，2 和 3）。
对于 nums[1]=1 不存在比它小的数字。
对于 nums[2]=2 存在一个比它小的数字：（1）。
对于 nums[3]=2 存在一个比它小的数字：（1）。
对于 nums[4]=3 存在三个比它小的数字：（1，2 和 2）。

Example 2：
输入：nums = [6,5,4,8]
输出：[2,1,0,3]

Example 3：
输入：nums = [7,7,7,7]
输出：[0,0,0,0]

Note：
2 <= nums.length <= 500
0 <= nums[i] <= 100
"""

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        tmp = []
        for idx, n in enumerate(nums):
            tmp.append([n, idx])
        s = list(sorted(tmp, key=lambda x: x[0]))
        ret = [0] * len(nums)
        sameTmp = {}
        for idx, item in enumerate(s):
            if item[0] in sameTmp:
                ret[item[1]] = sameTmp[item[0]]
                continue
            ret[item[1]] = idx
            sameTmp[item[0]] = idx
        return ret