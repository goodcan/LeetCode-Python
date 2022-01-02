#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/1/2 23:55
# @Author   : cancan
# @File     : method_1.py
# @Function : 一次编辑


"""
Question:
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

Example 1:
输入:
first = "pale"
second = "ple"
输出: True
 
Example 2:
输入:
first = "pales"
second = "pal"
输出: False
"""


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        l1 = len(first)
        l2 = len(second)

        if abs(l1 - l2) > 1:
            return False

        if l1 == l2:
            fn = 0
            for idx in range(l1):
                if fn > 1:
                    return False
                if first[idx] != second[idx]:
                    fn += 1
            return fn <= 1
        elif l1 > l2:
            for idx in range(l2):
                if first[idx] != second[idx]:
                    return first[idx + 1:] == second[idx:]
            return True
        elif l1 < l2:
            for idx in range(l1):
                if first[idx] != second[idx]:
                    return first[idx:] == second[idx + 1:]
            return True
