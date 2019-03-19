#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-19 17:10
# @Author   : cancan
# @File     : method_1.py
# @Function : 找到所有数组中消失的数字


"""
Question:
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
找到所有在 [1, n] 范围之间没有出现在数组中的数字。
您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

Example:
输入:
[4,3,2,7,8,2,3,1]
输出:
[5,6]
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        t = set()

        for i in nums:
            t.add(i)

        res = []

        for i in range(1, len(nums) + 1):
            if i not in t:
                res.append(i)

        return res
