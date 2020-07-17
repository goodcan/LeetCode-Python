#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/7/17 21:09
# @Author   : cancan
# @File     : method_1.py
# @Function : 旋转字符串

"""
给定两个字符串, A 和 B。
A 的旋转操作就是将 A 最左边的字符移动到最右边。 例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。如果在若干次旋转操作之后，A 能变成B，那么返回True。

示例 1:
输入: A = 'abcde', B = 'cdeab'
输出: true

示例 2:
输入: A = 'abcde', B = 'abced'
输出: false

注意：
A 和 B 长度不超过 100。
"""


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B:
            return True
        l = len(A)
        if l != len(B):
            return False
        for idx in range(l):
            if A[idx] == B[0]:
                d = l - idx
                if A[idx:] == B[:d] and A[:idx] == B[d:]:
                    return True
        return False
