#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-20 10:47
# @Author   : cancan
# @File     : method_1.py
# @Function : 单调数列


"""
Question:
如果数组是单调递增或单调递减的，那么它是单调的。
如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
当给定的数组 A 是单调数组时返回 true，否则返回 false。

Example 1：
输入：[1,2,2,3]
输出：true

Example 2：
输入：[6,5,4,4]
输出：true

Example 3：
输入：[1,3,2]
输出：false

Example 4：
输入：[1,2,4,5]
输出：true

Example 5：
输入：[1,1,1]
输出：true

Note：
1. 1 <= A.length <= 50000
2. -100000 <= A[i] <= 100000
"""


class Solution:
    def isMonotonic(self, A):
        l = len(A)

        if l <= 2:
            return True

        flag = None

        for i in range(l - 1):

            if flag is None:
                if A[i] > A[i + 1]:
                    flag = 1
                elif A[i] < A[i + 1]:
                    flag = 2
            elif flag == 1:
                if A[i] < A[i + 1]:
                    return False
            elif flag == 2:
                if A[i] > A[i + 1]:
                    return False

        return True
