#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/7/1 10:33
# @Author   : cancan
# @File     : method_1.py
# @Function : 子集

"""
Question:
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

Note：
解集不能包含重复的子集。

Example:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

from typing import List


class Solution:
    """
    通过选与不选构建满二叉状态树
    eg: [1, 2, 3]
        1 = 选；0 = 不选
    1      1          0
    2   1     0    1     0
    3  1 0   1 0  1 0   1 0
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        self.dfs(nums, 0, [], res)
        res.append([])
        return res

    def dfs(self, nums: List, index: int, subset: List[int], res: List[List[int]]):
        if index == len(nums):
            return

        subset = subset.copy()

        res.append(subset)
        self.dfs(nums, index + 1, subset, res)
        subset.append(nums[index])
        self.dfs(nums, index + 1, subset, res)
