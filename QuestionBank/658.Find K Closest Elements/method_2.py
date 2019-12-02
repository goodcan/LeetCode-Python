#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/12/2 17:12
# @Author   : cancan
# @File     : method_2.py
# @Function : 找到 K 个最接近的元素

"""
Question:
给定一个排序好的数组，两个整数 k 和 x，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。
如果有两个数与 x 的差值一样，优先选择数值较小的那个数。

Example 1:
输入: [1,2,3,4,5], k=4, x=3
输出: [1,2,3,4]
 
Example 2:
输入: [1,2,3,4,5], k=4, x=-1
输出: [1,2,3,4]

Note:
1.k 的值为正数，且总是小于给定排序数组的长度。
2.数组不为空，且长度不超过 104
3.数组里的每个元素与 x 的绝对值不超过 104
"""

import bisect
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = right = bisect.bisect_left(arr, x)
        while right - left < k:
            if left == 0: return arr[:k]
            if right == len(arr): return arr[-k:]
            if x - arr[left - 1] <= arr[right] - x:
                left -= 1
            else:
                right += 1
        return arr[left:right]
