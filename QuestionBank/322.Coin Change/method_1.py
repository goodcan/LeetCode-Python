#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/7/24 22:50
# @Author   : cancan
# @File     : method_1.py
# @Function : 零钱兑换

"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。

Example 1:
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

Example 2:
输入：coins = [2], amount = 3
输出：-1

Example 3:
输入：coins = [1], amount = 0
输出：0

Note:
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""

from typing import *


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        self.coins = coins
        self.count = {}
        return self.dp(amount)

    def dp(self, amount: int) -> int:
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if self.count.get(amount, 0) != 0:
            return self.count[amount]

        ans = -1
        for v in self.coins:
            tmp = self.dp(amount - v)
            if tmp >= 0:
                tmp += 1
                if ans == -1:
                    ans = tmp
                elif tmp < ans:
                    ans = tmp
        self.count[amount] = ans
        return self.count[amount]
