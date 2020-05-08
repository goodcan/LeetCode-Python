#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/8 14:41
# @Author   : cancan
# @File     : method_1.py
# @Function : 最大正方形

"""
Question:
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

Example:
输入:
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
输出: 4
"""

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        h = len(matrix)
        if h == 0:
            return 0
        w = len(matrix[0])
        ret = 0

        for i in range(h):
            for j in range(w):
                if matrix[i][j] == '0':
                    continue

                maxLen = min(h - i, w - j)
                size = 1

                for k in range(1, maxLen):
                    if matrix[i + k][j + k] == "0":
                        break

                    flag = True
                    for ii in range(i, i + k):
                        if matrix[ii][j + k] == '0':
                            flag = False
                            break

                    for jj in range(j, j + k):
                        if matrix[i + k][jj] == '0':
                            flag = False
                            break
                    if flag:
                        size += 1
                    else:
                        break

                if size > ret:
                    ret = size

        return ret * ret
