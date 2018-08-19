#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/31 15:01
# @Author   : cancan
# @File     : method_2.py
# @Function : 只出现一次的数字 II

"""
Question:
给定一个非空整数数组，除了某个元素只出现一次以外，
其余每个元素均出现了三次。找出那个只出现了一次的元素。

Note
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

Example 1:
输入: [2,2,3,2]
输出: 3

Example 2:
输入: [0,1,0,1,0,1,99]
输出: 99
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (3 * sum(set(nums)) - sum(nums)) // 2
