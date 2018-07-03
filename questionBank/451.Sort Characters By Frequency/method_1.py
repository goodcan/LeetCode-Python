#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/3 18:27
# @Author   : cancan
# @File     : method_1.py
# @Function : 根据字符出现频率排序

"""
Question:
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

Example 1:
输入:"tree"
输出:"eert"
解释:'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。

Example 2:
输入:"cccaaa"
输出:"cccaaa"
解释:'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。

Example 3:
输入:"Aabb"
输出:"bbAa"
解释:此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
注意'A'和'a'被认为是两种不同的字符。
"""


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        t = {}

        for i in s:
            if i in t:
                t[i] += 1
            else:
                t[i] = 1

        d = sorted(zip(t.keys(), t.values()), key=lambda x: x[1], reverse=True)

        r = ''
        for i in d:
            r += i[0] * i[1]

        return r
