#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-14 15:35
# @Author   : cancan
# @File     : method_1.py
# @Function : 除自身以外数组的乘积


"""
Question:
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

Example:
输入: [1,2,3,4]
输出: [24,12,8,6]

Note: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

Follow up：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        t = {}
        res = []

        for i, v in enumerate(nums):
            if v in t:
                res.append(t[v])
            else:
                p = 1
                for j in nums[:i]:
                    p *= j
                for j in nums[i + 1:]:
                    p *= j

                t[v] = p

                res.append(p)

        return res
