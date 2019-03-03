#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-03 22:18
# @Author   : cancan
# @File     : method_1.py
# @Function : 单词拆分

"""
Question:
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，
判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

Note：
1.拆分时可以重复使用字典中的单词。
2.你可以假设字典中没有重复的单词。

Example 1:
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

Example 2:
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。

Example 3:
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""


class Solution:
    def wordBreak(self, s, wordDict):

        breakIndex = [0]
        for i in range(len(s) + 1):
            for j in breakIndex:
                if s[j:i] in wordDict:
                    breakIndex.append(i)
                    break

        return breakIndex[-1] == len(s)
