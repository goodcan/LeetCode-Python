#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/5/7 10:11
# @Author   : cancan
# @File     : method_1.py
# @Function : 千位分隔数

"""
给你一个整数 n，请你每隔三位添加点（即 "." 符号）作为千位分隔符，并将结果以字符串格式返回。

Example 1：
输入：n = 987
输出："987"

Example 2：
输入：n = 1234
输出："1.234"

Example 3：
输入：n = 123456789
输出："123.456.789"

Example 4：
输入：n = 0
输出："0"
 
Note：
 - 0 <= n < 2^31
"""


class Solution:
    def thousandSeparator(self, n: int) -> str:
        ret = ''
        run = True
        while run:
            a, b = divmod(n, 1000)
            if a == 0:
                run = False
                ret = str(b) + '.' + ret
            else:
                ret = '%03d' % b + '.' + ret
            n = a

        return ret[:-1]
