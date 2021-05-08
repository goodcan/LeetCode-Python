#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2021/5/8 10:54
# @Author   : cancan
# @File     : method_1.py
# @Function : 最小K个数

"""
设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。

示例：
输入： arr = [1,3,5,7,2,4,6,8], k = 4
输出： [1,2,3,4]

提示：
0 <= len(arr) <= 100000
0 <= k <= min(100000, len(arr))
"""

from typing import List


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]
