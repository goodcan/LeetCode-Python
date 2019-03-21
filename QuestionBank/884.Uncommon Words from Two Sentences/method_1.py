#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-21 16:51
# @Author   : cancan
# @File     : method_1.py
# @Function : 两句话中的不常见单词


"""
Question:
给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）
如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。
返回所有不常用单词的列表。
您可以按任何顺序返回列表。

Example 1：
输入：A = "this apple is sweet", B = "this apple is sour"
输出：["sweet","sour"]

Example 2：
输入：A = "apple apple", B = "banana"
输出：["banana"]

Note：
0 <= A.length <= 200
0 <= B.length <= 200
A 和 B 都只包含空格和小写字母。
"""


class Solution:
    def uncommonFromSentences(self, A, B):
        A = A.split(' ')
        B = B.split(' ')

        d = {}

        for i in A + B:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        return [k for k, v in d.items() if v < 2]
