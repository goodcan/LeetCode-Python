#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/9/18 10:48
# @Author   : cancan
# @File     : method_1.py
# @Function : 全排列 II

"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.nums = sorted(nums)
        self.numsLen = len(self.nums)
        self.ret = []
        self.used = [False] * self.numsLen
        self.dfs([])
        return self.ret

    def dfs(self, l):
        if len(l) == self.numsLen:
            self.ret.append(l)
            return

        for idx in range(self.numsLen):
            if not self.used[idx]:
                if idx > 0 and self.nums[idx - 1] == self.nums[idx] and not self.used[idx - 1]:
                    continue
                self.used[idx] = True
                self.dfs(l + [self.nums[idx]])
                self.used[idx] = False
