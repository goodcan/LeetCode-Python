#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/6/10 23:36
# @Author   : cancan
# @File     : method_1.py
# @Function : 爱吃香蕉的珂珂

"""
珂珂喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 h 小时后回来。
珂珂可以决定她吃香蕉的速度 k （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 k 根。如果这堆香蕉少于 k 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  
珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。
返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）。

Example 1：
输入：piles = [3,6,7,11], h = 8
输出：4

Example 2：
输入：piles = [30,11,23,4,20], h = 5
输出：30

Example 3：
输入：piles = [30,11,23,4,20], h = 6
输出：23

Note：
- 1 <= piles.length <= 104
- piles.length <= h <= 109
- 1 <= piles[i] <= 109
"""

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right
        while left < right:
            mid = left + (right - left) // 2
            count = 0
            for v in piles:
                a, b = divmod(v, mid)
                count += a if b == 0 else a + 1
                if count > h:
                    break
            if count <= h:
                ans = mid
                right = mid
            else:
                left = mid + 1
        return ans
