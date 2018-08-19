#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/7 13:58
# @Author   : cancan
# @File     : method_1.py
# @Function : 前K个高频元素

"""
Question:
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

Example
给定数组 [1,1,1,2,2,3] , 和 k = 2，返回 [1,2]。

Note
1.你可以假设给定的 k 总是合理的，1 ≤ k ≤ 数组中不相同的元素的个数。
2.你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
"""


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        t = {i: 0 for i in set(nums)}

        for i in nums:
            t[i] += 1

        return [i[0] for i in
                sorted(t.items(), key=lambda x: x[1], reverse=True)[:k]]
