#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-21 16:19
# @Author   : cancan
# @File     : method_1.py
# @Function : 二进制间距


"""
Question:
给定一个正整数 N，找到并返回 N 的二进制表示中两个连续的 1 之间的最长距离。
如果没有两个连续的 1，返回 0 。

Example 1：
输入：22
输出：2
解释：
22 的二进制是 0b10110 。
在 22 的二进制表示中，有三个 1，组成两对连续的 1 。
第一对连续的 1 中，两个 1 之间的距离为 2 。
第二对连续的 1 中，两个 1 之间的距离为 1 。
答案取两个距离之中最大的，也就是 2 。

Example 2：
输入：5
输出：2
解释：
5 的二进制是 0b101 。

Example 3：
输入：6
输出：1
解释：
6 的二进制是 0b110 。

Example 4：
输入：8
输出：0
解释：
8 的二进制是 0b1000 。
在 8 的二进制表示中没有连续的 1，所以返回 0 。

Note：
1 <= N <= 10^9
"""


class Solution:
    def binaryGap(self, N: int) -> int:
        s = bin(N)[2:]

        start = 0

        l = len(s)

        ans = 0

        while start < l:
            j = start + 1

            while j < l:

                if s[j] == '1':
                    d = j - start

                    if d > ans:
                        ans = d

                    start = j
                    break

                j += 1

            if j == l:
                break

        return ans
