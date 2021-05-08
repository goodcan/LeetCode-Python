#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2021/5/8 10:34
# @Author   : cancan
# @File     : method_1.py
# @Function : 主要元素

"""
数组中占比超过一半的元素称之为主要元素。给定一个整数数组，找到它的主要元素。若没有，返回-1。

示例 1：
输入：[1,2,5,9,5,9,5,5,5]
输出：5

示例 2：
输入：[3,2]
输出：-1

示例 3：
输入：[2,2,1,1,1,2,2]
输出：2
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) // 2
        tmp = {}
        for v in nums:
            tmp[v] = tmp.get(v, 0) + 1
            if tmp[v] > n:
                return v

        return -1
