#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/5/7 10:19
# @Author   : cancan
# @File     : method_1.py
# @Function : 迷你语法分析器

"""
给定一个字符串 s 表示一个整数嵌套列表，实现一个解析它的语法分析器并返回解析的结果 NestedInteger 。
列表中的每个元素只可能是整数或整数嵌套列表

Example 1：
输入：s = "324",
输出：324
解释：你应该返回一个 NestedInteger 对象，其中只包含整数值 324。

Example 2：
输入：s = "[123,[456,[789]]]",
输出：[123,[456,[789]]]
解释：返回一个 NestedInteger 对象包含一个有两个元素的嵌套列表：
1. 一个 integer 包含值 123
2. 一个包含两个元素的嵌套列表：
    i.  一个 integer 包含值 456
    ii. 一个包含一个元素的嵌套列表
         a. 一个 integer 包含值 789
 
Note：
 - 1 <= s.length <= 5 * 104
 - s 由数字、方括号 "[]"、负号 '-' 、逗号 ','组成
 - 用例保证 s 是可解析的 NestedInteger
 - 输入中的所有值的范围是 [-106, 106]
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        nodes = []
        idx = 0
        num = ''
        ans = NestedInteger()
        for v in s:
            if v == ',':
                if num:
                    nodes[idx - 1].add(NestedInteger(int(num)))
                num = ''
                continue

            if v == '[':
                new = NestedInteger()
                if idx > 0:
                    nodes[idx - 1].add(new)
                nodes.append(new)
                idx += 1
                continue

            if v == ']':
                if num:
                    nodes[idx - 1].add(NestedInteger(int(num)))
                num = ''
                ans = nodes.pop()
                idx -= 1
                continue

            num += v

        if num:
            ans.setInteger(int(num))

        return ans
