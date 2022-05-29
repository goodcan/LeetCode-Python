#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/5/29 23:08
# @Author   : cancan
# @File     : method_1.py
# @Function : 单词距离

"""
有个内含单词的超大文本文件，给定任意两个不同的单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗?

Example：
输入：words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student"
输出：1

Note：
words.length <= 100000
"""

from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        pre = -1
        ans = float('inf')
        for idx, v in enumerate(words):
            if v == word1 or v == word2:
                if pre != -1 and words[pre] != v:
                    ans = min(ans, idx - pre)
                pre = idx
        return ans
