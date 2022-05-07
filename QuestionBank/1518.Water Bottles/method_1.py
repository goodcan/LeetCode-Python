#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/5/7 10:16
# @Author   : cancan
# @File     : method_1.py
# @Function : 换酒问题

"""
小区便利店正在促销，用 numExchange 个空酒瓶可以兑换一瓶新酒。你购入了 numBottles 瓶酒。
如果喝掉了酒瓶中的酒，那么酒瓶就会变成空的。
请你计算 最多 能喝到多少瓶酒。

Example 1：
输入：numBottles = 9, numExchange = 3
输出：13
解释：你可以用 3 个空酒瓶兑换 1 瓶酒。
所以最多能喝到 9 + 3 + 1 = 13 瓶酒。

Example 2：
输入：numBottles = 15, numExchange = 4
输出：19
解释：你可以用 4 个空酒瓶兑换 1 瓶酒。
所以最多能喝到 15 + 3 + 1 = 19 瓶酒。

Example 3：
输入：numBottles = 5, numExchange = 5
输出：6

Example 4：
输入：numBottles = 2, numExchange = 3
输出：2

Note：
 - 1 <= numBottles <= 100
 - 2 <= numExchange <= 100
"""


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        num = numBottles
        while num // numExchange > 0:
            a, b = divmod(num, numExchange)
            num = a + b
            ans += a
        return ans
