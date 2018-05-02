#!/usr/bin/env python
# @Time     : 2018/5/2 下午11:12
# @Author   : cancan
# @File     : method_1.py
# @Function : 旋转图像

"""
Question:
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。

Note:
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

Example 1:
给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        import copy
        p = copy.deepcopy(matrix)
        l = len(matrix)
        for x in range(l):
            for y in range(l):
                matrix[x][y] = p[l - y - 1][x]
