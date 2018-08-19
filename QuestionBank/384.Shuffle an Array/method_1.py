#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/24 20:38
# @Author   : cancan
# @File     : method_1.py
# @Function : 打乱数组

"""
Question:
打乱一个没有重复元素的数组。

Example:
// 以数字集合 1, 2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
solution.shuffle();

// 重设数组到它的初始状态[1,2,3]。
solution.reset();

// 随机返回数组[1,2,3]打乱后的结果。
solution.shuffle();
"""

from random import shuffle


class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.old = nums
        self.t = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.old

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        shuffle(self.t)
        return self.t

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
