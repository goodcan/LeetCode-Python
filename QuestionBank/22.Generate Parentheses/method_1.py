#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/4/10 9:42
# @Author   : cancan
# @File     : method_1.py
# @Function : 括号生成


"""
Question:
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

Example，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def generateParenthesis(self, n):
        ans = []

        def dfs(s='', left=0, right=0):
            if len(s) == 2 * n:
                ans.append(s)

            if left < n:
                dfs(s + '(', left + 1, right)

            if right < left:
                dfs(s + ')', left, right + 1)

        dfs()

        return ans
