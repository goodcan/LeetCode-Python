#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/9/27 14:20
# @Author   : cancan
# @File     : method_1.py
# @Function : 最大交换

"""
给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。

示例 1 :
输入: 2736
输出: 7236
解释: 交换数字2和数字7。

示例 2 :
输入: 9973
输出: 9973
解释: 不需要交换。

注意:
给定数字的范围是 [0, 108]
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        l = list(str(num))
        for i in range(len(l)):
            for j in range(i):
                l[i], l[j] = l[j], l[i]
                num = max(num, int(''.join(l)))
                l[i], l[j] = l[j], l[i]
        return num