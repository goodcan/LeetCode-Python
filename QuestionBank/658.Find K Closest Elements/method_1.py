#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/12/2 16:27
# @Author   : cancan
# @File     : method_1.py
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

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        tmpDict1 = {}
        tmpDict2 = {}
        tmpList = []
        for v in arr:
            d = v - x
            if d <= 0:
                d = abs(d)
                tmpDict1[d] = v
                tmpList.append((d, tmpDict1))
            else:
                d = abs(d)
                tmpDict2[d] = v
                tmpList.append((d, tmpDict2))

        tmpList.sort(key=lambda x: x[0])
        ret = []
        for v in tmpList[:k]:
            ret.append(v[1][v[0]])
        ret.sort()
        return ret
