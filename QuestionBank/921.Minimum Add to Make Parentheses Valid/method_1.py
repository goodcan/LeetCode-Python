#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/4/23 15:16
# @Author   : cancan
# @File     : method_1.py
# @Function : 使括号有效的最少添加


"""
Question:
给定一个由 '(' 和 ')' 括号组成的字符串 S，我们需要添加最少的括号（ '(' 或是 ')'，可以在任何位置），以使得到的括号字符串有效。
从形式上讲，只有满足下面几点之一，括号字符串才是有效的：

它是一个空字符串，或者
它可以被写成 AB （A 与 B 连接）, 其中 A 和 B 都是有效字符串，或者
它可以被写作 (A)，其中 A 是有效字符串。
给定一个括号字符串，返回为使结果字符串有效而必须添加的最少括号数。

Example 1：
输入："())"
输出：1

Example 2：
输入："((("
输出：3

Example 3：
输入："()"
输出：0

Example 4：
输入："()))(("
输出：4

Note：
S.length <= 1000
S 只包含 '(' 和 ')' 字符。
"""


class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        left = 0
        right = 0

        for i in S:
            if i == '(':
                left += 1
            else:
                if left > 0:
                    left -= 1
                else:
                    right += 1

        return left + right
