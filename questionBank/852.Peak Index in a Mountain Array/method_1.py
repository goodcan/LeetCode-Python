#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/6/26 11:50
# @Author   : cancan
# @File     : method_1.py
# @Function : 山脉数组的峰顶索引

"""
Question:
我们把符合下列属性的数组 A 称作山脉：
    A.length >= 3
    存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。

Example 1:
输入：[0,1,0]
输出：1

Example 2:
输入：[0,2,1,0]
输出：1

Note:
1. 3 <= A.length <= 10000
2. 0 <= A[i] <= 10^6
3. A 是如上定义的山脉
"""

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))