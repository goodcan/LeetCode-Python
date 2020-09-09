#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/9/9 11:06
# @Author   : cancan
# @File     : method_1.py
# @Function : 组合总和

"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。

示例1：
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]

示例2：
输入：candidates = [2,3,5], target = 8,
所求解集为：
[
 [2,2,2,2],
 [2,3,3],
 [3,5]
]

提示：
- 1 <= candidates.length <= 30
- 1 <= candidates[i] <= 200
- candidate 中的每个元素都是独一无二的。
- 1 <= target <= 500
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ret = []
        self.nums = candidates
        self.target = target
        self.dfs(0, 0, [])
        return self.ret

    def dfs(self, start, s, l):
        if s > self.target:
            return

        if s == self.target:
            self.ret.append(l)
            return

        for i, v in enumerate(self.nums[start:]):
            self.dfs(i + start, s + v, l + [v])
