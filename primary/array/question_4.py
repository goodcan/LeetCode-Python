#!/usr/bin/env python
# @Time     : 2018/4/10 下午10:22
# @Author   : cancan
# @File     : question_2.py
# @Function : 存在重复


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)
