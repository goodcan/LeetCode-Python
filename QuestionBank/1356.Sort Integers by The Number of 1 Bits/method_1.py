#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/11/6 14:36
# @Author   : cancan
# @File     : method_1.py
# @Function : 根据数字二进制下 1 的数目排序


"""
给你一个整数数组 arr。请你将数组中的元素按照其二进制表示中数字 1 的数目升序排序。
如果存在多个数字二进制中 1 的数目相同，则必须将它们按照数值大小升序排列。
请你返回排序后的数组。


示例 1：
输入：arr = [0,1,2,3,4,5,6,7,8]
输出：[0,1,2,4,8,3,5,6,7]
解释：[0] 是唯一一个有 0 个 1 的数。
[1,2,4,8] 都有 1 个 1 。
[3,5,6] 有 2 个 1 。
[7] 有 3 个 1 。
按照 1 的个数排序得到的结果数组为 [0,1,2,4,8,3,5,6,7]

示例 2：
输入：arr = [1024,512,256,128,64,32,16,8,4,2,1]
输出：[1,2,4,8,16,32,64,128,256,512,1024]
解释：数组中所有整数二进制下都只有 1 个 1 ，所以你需要按照数值大小将它们排序。

示例 3：
输入：arr = [10000,10000]
输出：[10000,10000]

示例 4：
输入：arr = [2,3,5,7,11,13,17,19]
输出：[2,3,5,17,7,11,13,19]

示例 5：
输入：arr = [10,100,1000,10000]
输出：[10,100,10000,1000]

提示：
1 <= arr.length <= 500
0 <= arr[i] <= 10^4
"""

from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        data = {}

        for item in arr:
            n = self.calcBin1Num(item)
            data.setdefault(n, [])
            data[n].append(item)

        ret = []
        for k in sorted(data.keys()):
            ret.extend(sorted(data[k]))

        return ret

    def calcBin1Num(self, num: int) -> int:
        ret = 0
        for i in bin(num)[2:]:
            if i == '1':
                ret += 1
        return ret
