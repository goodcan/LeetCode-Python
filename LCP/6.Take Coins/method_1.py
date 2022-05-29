#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2021/2/20 11:50
# @Author   : cancan
# @File     : method_1.py
# @Function : 拿硬币

"""
桌上有 n 堆力扣币，每堆的数量保存在数组 coins 中。我们每次可以选择任意一堆，拿走其中的一枚或者两枚，求拿完所有力扣币的最少次数。

示例 1：
输入：[4,2,1]
输出：4
解释：第一堆力扣币最少需要拿 2 次，第二堆最少需要拿 1 次，第三堆最少需要拿 1 次，总共 4 次即可拿完。

示例 2：
输入：[2,3,10]
输出：8

限制：
- 1 <= n <= 4
- 1 <= coins[i] <= 10
"""

from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        ans = 0
        for v in coins:
            div, mod = divmod(v, 2)
            ans += div
            if mod > 0:
                ans += 1
        return ans
