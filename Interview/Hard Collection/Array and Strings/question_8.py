#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/10 11:09
# @Author   : cancan
# @File     : question_8.py
# @Function : 寻找重复数

"""
Question:
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），
可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

Example 1:
输入: [1,3,4,2,2]
输出: 2

Example 2:
输入: [3,1,3,4,2]
输出: 3

Note：
1.不能更改原数组（假设数组是只读的）。
2.只能使用额外的 O(1) 的空间。
3.时间复杂度小于 O(n2) 。
4.数组中只有一个重复的数字，但它可能不止重复出现一次。
"""


class Solution1(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = {}

        for i in nums:
            if i in t:
                return i
            else:
                t[i] = 1


class Solution2(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        d = len(nums) - len(s)
        return (sum(nums) - sum(s)) // d
