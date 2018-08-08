#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/8 18:16
# @Author   : cancan
# @File     : question_8.py
# @Function : 搜索二维矩阵 II

"""
Question:
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
1.每行的元素从左到右升序排列。
2.每列的元素从上到下升序排列。

Example:
现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。
给定 target = 20，返回 false。
"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for item in matrix:
            if target in item:
                return True
        return False
