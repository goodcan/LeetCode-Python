#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/11/3 10:04
# @Author   : cancan
# @File     : method_1.py
# @Function : 有效的山脉数组

"""
给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。
让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

A.length >= 3
在 0 < i A.length - 1 条件下，存在 i 使得：
    A[0] < A[1] < ... A[i-1] < A[i]
    A[i] > A[i+1] > ... > A[A.length - 1]

示例 1：
输入：[2,1]
输出：false

示例 2：
输入：[3,5,5]
输出：false

示例 3：
输入：[0,3,2,1]
输出：true

提示：
0 <= A.length <= 10000
0 <= A[i] <= 10000
"""

from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        l = len(A)
        if l <= 2:
            return False

        # 1 上升
        # 2 下降
        flag = 1
        count1 = 0
        i = 1
        for idx in range(1, l):
            i = idx
            if flag == 1 and A[idx - 1] >= A[i]:
                flag = 2

            if flag == 1:
                count1 += 1

            if flag == 2 and A[idx - 1] <= A[i]:
                return False

        if count1 == 0 or flag == 1:
            return False

        return True
