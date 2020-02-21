#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/21 11:33
# @Author   : cancan
# @File     : method_1.py
# @Function : 判定字符是否唯一

'''
Question:
实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

Example 1：
输入: s = "leetcode"
输出: false

Example 2：
输入: s = "abc"
输出: true

Note：
1. 0 <= len(s) <= 100
2. 如果你不使用额外的数据结构，会很加分。
'''

class Solution:
    def isUnique(self, astr: str) -> bool:
        return len(set(astr)) == len(list(astr))
