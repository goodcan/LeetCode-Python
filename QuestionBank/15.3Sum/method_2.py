#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-01-15 10:27
# @Author   : cancan
# @File     : method_2.py
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

        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1

        # 处理三个 0 的特殊情况
        if 0 in dic and dic[0] >= 3:
            r = [[0, 0, 0]]
        else:
            r = []

        # 核心处理，分离正负数
        pos = []
        neg = []
        for n in dic:
            if n > 0:
                pos.append(n)
            elif n < 0:
                neg.append(n)

        for p in pos:
            for n in neg:
                t = - (p + n)
                if t in dic:
                    if t == p and dic[p] > 1:
                        r.append([n, p, p])
                    elif t == n and dic[n] > 1:
                        r.append([n, n, p])

                    # 这一步很关键
                    # 过滤了 1 倍的重复情况
                    # eg: -1, -2, 3
                    # 大小判断，必须是，t 负数则要小于 neg，t 是正数则要大于 pos
                    # 这么做防止出现，负数小于正数，正数大于负数，跨越 0 的界限
                    elif t < n or t > p or t == 0:
                        r.append([n, t, p])

        return r
