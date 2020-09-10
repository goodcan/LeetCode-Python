#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/9/11 0:52
# @Author   : cancan
# @File     : method_1.py
# @Function : 组合总和 III

"""
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：
- 所有数字都是正整数。
- 解集不能包含重复的组合。

示例 1:
输入: k = 3, n = 7
输出: [[1,2,4]]

示例 2:
输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
"""

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.k = k
        self.n = n
        self.ret = []
        self.dfs(1, 0, [])
        return self.ret

    def dfs(self, start, s, l):
        if len(l) > self.k:
            return

        if s > self.n:
            return

        if len(l) == self.k and s == self.n:
            self.ret.append(l)
            return

        for i in range(start, 10):
            self.dfs(i + 1, s + i, l + [i])
