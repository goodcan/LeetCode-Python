#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-04 09:44
# @Author   : cancan
# @File     : method_1.py
# @Function : 单词拆分 II


"""
Question:
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，
在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

Note
1.分隔时可以重复使用字典中的单词。
2.你可以假设字典中没有重复的单词。

Example 1：
输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]

Example 2：
输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。

Example 3：
输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]
"""


class Solution:
    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict)
        breakIndex = [0]
        for i in range(len(s) + 1):
            for j in breakIndex:
                if s[j:i] in wordDict:
                    breakIndex.append(i)
                    break
        res = []

        if breakIndex[-1] != len(s):
            return res

        self.dfs(s, len(s), wordDict, res, 0, [], set(breakIndex))

        return res

    def dfs(self, s, l, wordDict, res, start, temp, dp):

        if start == l:
            res.append(' '.join(temp))
            return

        for i in range(l):
            index = start + i + 1
            st = s[start:index]
            if index in dp and st in wordDict:
                temp.append(st)
                self.dfs(s, l, wordDict, res, index, temp, dp)
                temp.pop()
