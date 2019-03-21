#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-21 14:19
# @Author   : cancan
# @File     : method_1.py
# @Function : 三角形的最大周长


"""
Question:
给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
如果不能形成任何面积不为零的三角形，返回 0。

Example 1：
输入：[2,1,2]
输出：5

Example 2：
输入：[1,2,1]
输出：0

Example 3：
输入：[3,2,3,4]
输出：10

Example 4：
输入：[3,6,2,3]
输出：8

Note：
    * 3 <= A.length <= 10000
    * 1 <= A[i] <= 10^6
"""


class Solution:
    def largestPerimeter(self, A):

        l = len(A)

        if l <= 2:
            return 0

        ans = 0

        A.sort(reverse=True)

        for i in range(l - 2):
            d = A[i] - A[i + 1]

            if A[i + 2] > d:
                return A[i] + A[i + 1] + A[i + 2]

        return ans
