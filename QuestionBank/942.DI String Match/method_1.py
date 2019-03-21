#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-21 14:41
# @Author   : cancan
# @File     : method_1.py
# @Function : 增减字符串匹配


"""
Question:
给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。
返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有：
如果 S[i] == "I"，那么 A[i] < A[i+1]
如果 S[i] == "D"，那么 A[i] > A[i+1]

Example 1：
输出："IDID"
输出：[0,4,1,3,2]

Exmaple 2：
输出："III"
输出：[0,1,2,3]

Example 3：
输出："DDI"
输出：[3,2,0,1]

Note：
1. 1 <= S.length <= 1000
2. S 只包含字符 "I" 或 "D"。
"""


class Solution:
    def diStringMatch(self, S):
        N = len(S)

        ans = [i for i in range(N + 1)]

        for i, v in enumerate(S):

            if v == 'D':
                ans.insert(i, ans.pop())

        return ans
