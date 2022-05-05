#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/5/5 10:55
# @Author   : cancan
# @File     : method_1.py
# @Function : 单词转换

"""
Question:
给定字典中的两个词，长度相等。写一个方法，把一个词转换成另一个词， 但是一次只能改变一个字符。每一步得到的新词都必须能在字典中找到。
编写一个程序，返回一个可能的转换序列。如有多个可能的转换序列，你可以返回任何一个。

Example 1:
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
输出:
["hit","hot","dot","lot","log","cog"]

Example 2:
输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
输出: []
解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
"""

from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        self.tmp = {}
        ans = self.dfs(beginWord, endWord, wordList)
        if ans:
            ans.insert(0, beginWord)
        return ans

    def dfs(self, beginWord, endWord, wordList):
        ans = []
        for idx, v in enumerate(wordList):
            if v in self.tmp:
                continue

            if not self.checkDiffOne(beginWord, v):
                continue

            ans.append(v)
            self.tmp[v] = True

            if endWord == v:
                return ans

            tmp = wordList[::]
            result = self.dfs(v, endWord, tmp[:idx] + tmp[idx + 1:])
            if result:
                ans.extend(result)

            if ans[-1] == endWord:
                return ans
            else:
                ans = []

        return ans

    def checkDiffOne(self, a, b):
        if len(a) != len(b):
            return False

        count = 0
        for idx in range(len(a)):
            if a[idx] != b[idx]:
                count += 1

            if count > 1:
                return False

        return count == 1
