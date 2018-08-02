#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/2 16:17
# @Author   : cancan
# @File     : method_2.py
# @Function : 颜色分类

"""
Question:
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，
使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

Note:
不能使用代码库中的排序函数来解决这道题。

Example:
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]

Follow up
1.一个直观的解决方案是使用计数排序的两趟扫描算法。首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
2.你能想出一个仅使用常数空间的一趟扫描算法吗？
"""


class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n0, n1, n2 = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[n2] = 2
                nums[n1] = 1
                nums[n0] = 0
                n0 += 1
                n1 += 1
                n2 += 1
            elif nums[i] == 1:
                nums[n2] = 2
                nums[n1] = 1
                n1 += 1
                n2 += 1
            elif nums[i] == 2:
                nums[n2] = 2
                n2 += 1
