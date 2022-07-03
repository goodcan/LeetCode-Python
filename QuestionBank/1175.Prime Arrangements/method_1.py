#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/7/3 21:52
# @Author   : cancan
# @File     : method_1.py
# @Function : 质数排列

"""
请你帮忙给从 1 到 n 的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。
让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。
由于答案可能会很大，所以请你返回答案 模 mod 10^9 + 7 之后的结果即可。

Example 1:
输入：n = 5
输出：12
解释：举个例子，[1,2,5,4,3] 是一个有效的排列，但 [5,2,3,4,1] 不是，因为在第二种情况里质数 5 被错误地放在索引为 1 的位置上。
Example 2:
输入：n = 100
输出：682289015

Note:
- 1 <= n <= 100
"""


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        tmp = [1] * n
        start = 1
        count = 0
        while start < n:
            start += 1
            a = 1
            idx = start * a
            if idx <= n and tmp[idx - 1] == 1:
                count += 1
            while idx <= n:
                tmp[idx - 1] = idx
                a += 1
                idx = start * a

        aa = 1
        ac = count
        while ac > 1:
            aa *= ac
            ac -= 1
        bb = 1
        bc = n - count
        while bc > 1:
            bb *= bc
            bc -= 1
        return aa * bb % (10 ** 9 + 7)
