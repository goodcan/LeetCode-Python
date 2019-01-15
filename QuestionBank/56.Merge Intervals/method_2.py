#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-01-15 22:49
# @Author   : cancan
# @File     : method_1.py
# @Function : 合并区间

"""
Question:
给出一个区间的集合，请合并所有重叠的区间。

Example 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

Example 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []

        for item in sorted(intervals, key=lambda x: x.start):
            if res and item.start <= res[-1].end:
                res[-1].end = max(res[-1].end, item.end)
            else:
                res.append(item)

        return res
