#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/2 19:06
# @Author   : cancan
# @File     : method_1.py
# @Function : 杨辉三角

"""
Question:
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

Example:
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = [[1]]
        r = [1, 1]
        for i in range(1, numRows):
            res.append(r)
            t = [1]
            for x in range(len(r) - 1):
                t.append(r[x] + r[x + 1])
            t.append(1)
            r = t

        return res

