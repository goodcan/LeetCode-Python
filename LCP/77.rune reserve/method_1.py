#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/25 11:11
# @Author   : cancan
# @File     : method_1.py
# @Function : 符文储备


"""
遠征隊在出發前需要攜帶一些「符文」，作為後續的冒險儲備。runes[i] 表示第 i 枚符文的魔力值。
他們將從中選取若干符文進行攜帶，並對這些符文進行重新排列，以確保任意相鄰的兩塊符文之間的魔力值相差不超過 1。

請返回他們能夠攜帶的符文 最大數量。

示例 1：
輸入：runes = [1,3,5,4,1,7]
輸出：3
解釋：最佳的選擇方案為[3,5,4] 將其排列為 [3,4,5] 後，任意相鄰的兩塊符文魔力值均不超過 1，攜帶數量為 3 其他滿足條件的方案為 [1,1] 和 [7]，數量均小於 3。 因此返回可攜帶的最大數量 3。

示例 2：
輸入：runes = [1,1,3,3,2,4]
輸出：6
解釋：排列為 [1,1,2,3,3,4]，可攜帶所有的符文

提示：
1 <= runes.length <= 10^4
0 <= runes[i] <= 10^4
"""

from typing import List


class Solution:
    def runeReserve(self, runes: List[int]) -> int:
        runes = sorted(runes)
        right = 1
        ans = 1
        while right < len(runes):
            tmp = 1
            while right < len(runes):
                if runes[right] - runes[right - 1] <= 1:
                    tmp += 1
                else:
                    break
                right += 1

            if tmp > ans:
                ans = tmp
            right += 1

        return ans
