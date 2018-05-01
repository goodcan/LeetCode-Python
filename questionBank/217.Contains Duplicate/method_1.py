#!/usr/bin/env python
# @Time     : 2018/4/10 下午10:22
# @Author   : cancan
# @File     : method_1.py
# @Function : 存在重复

"""
Question:
给定一个整数数组，判断是否存在重复元素。
如果任何值在数组中出现至少两次，函数应该返回 true。如果每个元素都不相同，则返回 false。
"""


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)
