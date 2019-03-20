#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-20 10:00
# @Author   : cancan
# @File     : method_1.py
# @Function : 数字转换为十六进制数


"""
Question:
给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。

Note:
1.十六进制中所有字母(a-f)都必须是小写。
2.十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。
3.给定的数确保在32位有符号整数范围内。
4.不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。

Example 1：
输入:
26

输出:
"1a"

Example 2：
输入:
-1

输出:
"ffffffff"
"""


class Solution:
    def toHex(self, num: int) -> str:
        d = {
            0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
            8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'
        }

        r = ''

        if num > 0:

            while num:
                a, b = divmod(num, 16)
                r = d[b] + r
                num = a

        elif num == 0:
            return '0'

        else:
            num = int((bin(((1 << 32) - 1) & num)[2:]).zfill(32), 2)
            return self.toHex(num)

        return r
