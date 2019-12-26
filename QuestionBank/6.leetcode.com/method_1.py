#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/12/26 16:56
# @Author   : cancan
# @File     : method_1.py
# @Function : Z 字形变换


"""
Question:
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
    L   C   I   R
    E T O E S I I G
    E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);

Example 1:
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"

Example 2:
输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:
    L     D     R
    E   O E   I I
    E C   I H   N
    T     S     G
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        tmp = {}
        for i in range(numRows):
            tmp[i] = []

        flag1 = 0
        flag2 = 0
        for v in s:
            if (flag2 == 0 and flag1 == numRows) or (flag2 == 1 and flag1 == numRows - 2):
                flag1 = 0
                if numRows > 2:
                    flag2 = 0 if flag2 == 1 else 1

            if flag2 == 0:
                tmp[flag1].append(v)
            else:
                tmp[numRows - 1 - flag1 - 1].append(v)

            flag1 += 1

        return ''.join([''.join(x) for x in tmp.values()])
