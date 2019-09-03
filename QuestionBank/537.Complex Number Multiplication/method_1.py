#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/3 18:12
# @Author   : cancan
# @File     : method_1.py
# @Function : 复数乘法

"""
Question:
给定两个表示复数的字符串。
返回表示它们乘积的字符串。注意，根据定义 i2 = -1 。

Example 1:
输入: "1+1i", "1+1i"
输出: "0+2i"
解释: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。

Example 2:
输入: "1+-1i", "1+-1i"
输出: "0+-2i"
解释: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。

Note:
输入字符串不包含额外的空格。
输入字符串将以 a+bi 的形式给出，其中整数 a 和 b 的范围均在 [-100, 100] 之间。输出也应当符合这种形式。
"""


class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        aSplit = a.split('+')
        bSplit = b.split('+')

        aX, aY = int(aSplit[0]), int(aSplit[1][:-1])
        bX, bY = int(bSplit[0]), int(bSplit[1][:-1])

        ansX = aX * bX - aY * bY
        ansY = aX * bY + aY * bX

        return str(ansX) + '+' + str(ansY) + 'i'
