#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/27 10:53
# @Author   : cancan
# @File     : method_1.py
# @Function : 和可被 K 整除的子数组


"""
Question:
给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。

Example：
输入：A = [4,5,0,-2,-3,1], K = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Note：
1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
"""

from typing import List

"""
思路：前缀和
p[i] = a[0[ + a[1] + a[2] + ... + a[i]
p[i, j] = p[j] - p[i - 1]
p[i, j] % k = 0
p[j] % k - p[i - 1] % k = 0
p[j] % k = p[i - 1] % k
"""


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        tmp = {0: 1}
        total, ans = 0, 0
        for v in A:
            total += v
            m = total % K
            ans += tmp.get(m, 0)
            tmp[m] = tmp.get(m, 0) + 1
        return ans
