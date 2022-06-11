#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/6/11 22:40
# @Author   : cancan
# @File     : method_1.py
# @Function : 森林中的兔子

"""
森林中有未知数量的兔子。提问其中若干只兔子 "还有多少只兔子与你（指被提问的兔子）颜色相同?" ，将答案收集到一个整数数组 answers 中，其中 answers[i] 是第 i 只兔子的回答。
给你数组 answers ，返回森林中兔子的最少数量。

Example 1：
输入：answers = [1,1,2]
输出：5
解释：
两只回答了 "1" 的兔子可能有相同的颜色，设为红色。
之后回答了 "2" 的兔子不会是红色，否则他们的回答会相互矛盾。
设回答了 "2" 的兔子为蓝色。
此外，森林中还应有另外 2 只蓝色兔子的回答没有包含在数组中。
因此森林中兔子的最少数量是 5 只：3 只回答的和 2 只没有回答的。

Example 2：
输入：answers = [10,10,10]
输出：11

Note：
- 1 <= answers.length <= 1000
- 0 <= answers[i] < 1000
"""

from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        tmp = {}
        count = {}
        n0 = 0
        for v in answers:
            if v == 0:
                n0 += 1
                continue

            tmp.setdefault(v, 0)
            tmp[v] += 1

        ans = n0
        for k, v in tmp.items():
            ans += (v + k) // (k + 1) * (k + 1)

        return ans
