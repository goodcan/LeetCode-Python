#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-21 14:33
# @Author   : cancan
# @File     : method_1.py
# @Function : 重复 N 次的元素


"""
Question:
在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。
返回重复了 N 次的那个元素。

Example 1：
输入：[1,2,3,3]
输出：3

Example 2：
输入：[2,1,2,5,3,2]
输出：2

Example 3：
输入：[5,1,5,2,5,3,5,4]
输出：5

Note：
1. 4 <= A.length <= 10000
2. 0 <= A[i] < 10000
3. A.length 为偶数
"""


class Solution:
    def repeatedNTimes(self, A):
        N = len(A) / 2

        d = {}

        for i in A:
            if i in d:
                d[i] += 1
                if d[i] == N:
                    return i
            else:
                d[i] = 1
