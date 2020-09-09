#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/9/9 18:38
# @Author   : cancan
# @File     : method_1.py
# @Function : 组合

"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ret = []
        self.n = n
        self.k = k
        self.dfs(1, [])
        return self.ret

    def dfs(self, start, l):
        if len(l) > self.k:
            return

        if len(l) == self.k:
            self.ret.append(l)
            return

        for i in range(start, self.n + 1):
            self.dfs(i + 1, l + [i])
