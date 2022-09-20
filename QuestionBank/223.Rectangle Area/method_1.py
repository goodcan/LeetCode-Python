#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/9/20 11:48
# @Author   : cancan
# @File     : method_1.py
# @Function : 矩形面积

"""
给你 二维 平面上两个 由直线构成且边与坐标轴平行/垂直 的矩形，请你计算并返回两个矩形覆盖的总面积。
每个矩形由其 左下 顶点和 右上 顶点坐标表示：
第一个矩形由其左下顶点 (ax1, ay1) 和右上顶点 (ax2, ay2) 定义。
第二个矩形由其左下顶点 (bx1, by1) 和右上顶点 (bx2, by2) 定义。

示例 1：
输入：ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
输出：45

示例 2：
输入：ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
输出：16

提示：
-104 <= ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 <= 104
"""

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        s = 0
        if bx1 >= ax2 or bx2 <= ax1 or by1 >= ay2 or by2 <= ay1:
            s = 0
        else:
            x1, x2 = sorted([ax1, ax2, bx1, bx2])[1:3]
            y1, y2 = sorted([ay1, ay2, by1, by2])[1:3]
            s = self.calc(x1, x2, y1, y2)
        print(s)
        return self.calc(ax1, ax2, ay1, ay2) + self.calc(bx1, bx2, by1, by2) - s


    def calc(self, x1, x2, y1, y2):
        return abs(x1 - x2) * abs(y1 - y2)