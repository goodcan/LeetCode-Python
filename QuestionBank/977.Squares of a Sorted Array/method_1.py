#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-21 10:20
# @Author   : cancan
# @File     : method_1.py
# @Function : 有序数组的平方


"""
Question:
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

Example 1：
输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]

Example 2：
输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]

Note：
* 1 <= A.length <= 10000
* -10000 <= A[i] <= 10000
* A 已按非递减顺序排序。
"""


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = [i ** 2 for i in A]
        res.sort()
        return res
