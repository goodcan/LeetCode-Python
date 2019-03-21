#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-21 16:29
# @Author   : cancan
# @File     : method_1.py
# @Function : 按奇偶排序数组


"""
Question:
给定一个非负整数数组 A，返回一个由 A 的所有偶数元素组成的数组，后面跟 A 的所有奇数元素。
你可以返回满足此条件的任何数组作为答案。

Example：
输入：[3,1,2,4]
输出：[2,4,3,1]
输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。

Note：
1 <= A.length <= 5000
0 <= A[i] <= 5000
"""


class Solution:
    def sortArrayByParity(self, A):
        ans = []

        for i in A:

            if i % 2 == 0:
                ans.insert(0, i)
            else:
                ans.append(i)

        return ans
