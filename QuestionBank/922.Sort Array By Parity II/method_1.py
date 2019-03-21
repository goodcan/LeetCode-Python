#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-21 15:03
# @Author   : cancan
# @File     : method_1.py
# @Function : 按奇偶排序数组 II


"""
Question:
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
你可以返回任何满足上述条件的数组作为答案。

Example：
输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。

Note：
1. 2 <= A.length <= 20000
2. A.length % 2 == 0
3. 0 <= A[i] <= 1000
"""


class Solution:
    def sortArrayByParityII(self, A):
        ans = [0] * len(A)

        s1 = 0
        s2 = 1

        for i in A:

            if i % 2 == 0:
                ans[s1] = i
                s1 += 2
            else:
                ans[s2] = i
                s2 += 2

        return ans
