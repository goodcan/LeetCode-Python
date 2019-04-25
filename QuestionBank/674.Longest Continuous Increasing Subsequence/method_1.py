#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/4/25 11:36
# @Author   : cancan
# @File     : method_1.py
# @Function : 最长连续递增序列


"""
Question:
给定一个未经排序的整数数组，找到最长且连续的的递增序列。

Example 1:
输入: [1,3,5,4,7]
输出: 3
解释: 最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。

Example 2:
输入: [2,2,2,2,2]
输出: 1
解释: 最长连续递增序列是 [2], 长度为1。

Note：数组长度不会超过10000。
"""


class Solution:
    def findLengthOfLCIS(self, nums):
        l = len(nums)

        if l in [0, 1]:
            return l

        start = 0
        end = 1
        ans = end - start

        while end < l:
            if nums[end] <= nums[end - 1]:
                if end - start > ans:
                    ans = end - start

                start = end
                end = start + 1

            else:
                end += 1

        if end - start > ans:
            ans = end - start

        return ans
