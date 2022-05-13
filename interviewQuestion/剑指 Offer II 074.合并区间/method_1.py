#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/5/13 22:12
# @Author   : cancan
# @File     : method_1.py
# @Function : 合并区间

"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

Example 1：
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

Example 2：
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

Note：
- 1 <= intervals.length <= 104
- intervals[i].length == 2
- 0 <= starti <= endi <= 104
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        ans = [intervals[0]]
        idx = 0

        for item in intervals[1:]:
            """
            ab   | a b  |  ab  | a  b |  a b |   ab
              xy |  x y | x  y |  xy  | x y  | xy
            """
            a, b = ans[idx]
            x, y = item
            if x > b:
                ans.append(item)
                idx += 1
            elif x == b:
                ans[idx] = [a, y]
            elif y < a:
                ans.insert(0, item)
                idx += 1
            elif y == a:
                ans[idx] = [x, b]
            elif a <= x and b >= x and b <= y:
                ans[idx] = [a, y]
            elif x <= a and b <= y:
                ans[idx] = [x, y]
            elif x <= a and a <= y and y <= b:
                ans[idx] = [x, b]
            elif x <= a and y >= b:
                ans[idx] = [x, y]
        return ans
