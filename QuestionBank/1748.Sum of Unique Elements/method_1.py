#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/5/7 10:05
# @Author   : cancan
# @File     : method_1.py
# @Function : 唯一元素的和

"""
给你一个整数数组 nums 。数组中唯一元素是那些只出现 恰好一次 的元素。
请你返回 nums 中唯一元素的 和 。

Example 1：
输入：nums = [1,2,3,2]
输出：4
解释：唯一元素为 [1,3] ，和为 4 。

Example 2：
输入：nums = [1,1,1,1,1]
输出：0
解释：没有唯一元素，和为 0 。

Example 3 ：
输入：nums = [1,2,3,4,5]
输出：15
解释：唯一元素为 [1,2,3,4,5] ，和为 15 。

提示：
 - 1 <= nums.length <= 100
 - 1 <= nums[i] <= 100
"""


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ret = 0
        tmp = {}
        for v in nums:
            if v not in tmp:
                ret += v
                tmp[v] = 1
            else:
                if tmp[v] == 1:
                    ret -= v
                    tmp[v] = -1
        return ret
