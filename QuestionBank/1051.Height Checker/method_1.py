#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/28 11:06
# @Author   : cancan
# @File     : method_1.py
# @Function : 高度检查器

"""
Question:
学校在拍年度纪念照时，一般要求学生按照 非递减 的高度顺序排列。
请你返回至少有多少个学生没有站在正确位置数量。该人数指的是：能让所有学生以 非递减 高度排列的必要移动人数。

Example：
输入：[1,1,4,2,1,3]
输出：3
解释：
高度为 4、3 和最后一个 1 的学生，没有站在正确的位置。

Note：
1 <= heights.length <= 100
1 <= heights[i] <= 100
"""


class Solution:
    def heightChecker(self, heights):
        tmp = sorted(heights)
        ans = 0

        for i, v in enumerate(heights):
            if v != tmp[i]:
                ans += 1

        return ans
