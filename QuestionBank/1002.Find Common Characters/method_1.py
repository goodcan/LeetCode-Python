#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-06-23 12:53
# @Author   : cancan
# @File     : method_1.py
# @Function : 查找常用字符

"""
Question:
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）
组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
你可以按任意顺序返回答案。

Example 1：
输入：["bella","label","roller"]
输出：["e","l","l"]

Example 2：
输入：["cool","lock","cook"]
输出：["c","o"]
 
Note：
1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] 是小写字母
"""


class Solution:
    def commonChars(self, A):
        tmp1 = {}

        for v in A.pop():
            tmp1.setdefault(v, 0)
            tmp1[v] += 1

        while len(A) != 0:
            a = A.pop()
            tmp2 = {}
            for v in a:
                tmp2.setdefault(v, 0)
                tmp2[v] += 1

            tmp3 = {}
            for k, v in tmp2.items():
                if k in tmp1:
                    tmp3[k] = tmp1[k]

                    if v < tmp1[k]:
                        tmp3[k] = v

            tmp1 = tmp3

        ret = []

        for k, v in tmp1.items():
            ret.extend([k] * v)

        return ret
