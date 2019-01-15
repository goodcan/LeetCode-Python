#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-01-15 10:27
# @Author   : cancan
# @File     : method_1.py
# @Function : 三数之和

"""
Questions:
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

Note：
答案中不可以包含重复的三元组。

Example,
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        t = set()
        res = []
        l = len(nums)

        for i in range(l):
            ii = i + 1
            iii = l - 1
            while (ii < iii):
                s = nums[i] + nums[ii] + nums[iii]

                if s == 0:

                    d = [nums[i], nums[ii], nums[iii]]
                    dd = ''.join(str(j) for j in d)
                    if dd not in t:
                        t.add(dd)
                        res.append(d)

                if s <= 0:
                    ii += 1
                else:
                    iii -= 1

        return list(res)
