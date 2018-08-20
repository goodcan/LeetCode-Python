#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/20 10:59
# @Author   : cancan
# @File     : question_3.py
# @Function : 两数之和 II - 输入有序数组

"""
Question:
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

NOte:
1.返回的下标值（index1 和 index2）不是从零开始的。
2.你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

Example:
输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        t = {}
        for i, v in enumerate(numbers):
            if v in t:
                return [t[v] + 1, i + 1]
            else:
                t[target - v] = i
