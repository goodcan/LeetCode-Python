#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/2 18:59
# @Author   : cancan
# @File     : method_1.py
# @Function : 杨辉三角 II

"""
Question:
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

Example:
输入: 3
输出: [1,3,3,1]

Follow up:
你可以优化你的算法到 O(k) 空间复杂度吗？
"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        r = [1, 1]
        for i in range(1, rowIndex):
            t = [1]
            for x in range(len(r) - 1):
                t.append(r[x] + r[x + 1])
            t.append(1)
            r = t

        return r
