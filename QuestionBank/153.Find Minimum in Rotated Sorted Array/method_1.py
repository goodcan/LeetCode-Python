#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/11/29 18:18
# @Author   : cancan
# @File     : method_1.py
# @Function : 寻找旋转排序数组中的最小值

"""
Question:
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
请找出其中最小的元素。
你可以假设数组中不存在重复元素。

Example 1:
输入: [3,4,5,1,2]
输出: 1

Example 2:
输入: [4,5,6,7,0,1,2]
输出: 0
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
