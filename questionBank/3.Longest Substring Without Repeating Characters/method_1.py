#!/usr/bin/python

"""
Question:
给定一个字符串，查找没有重复字符的最长子字符串的长度。

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.

Note 答案必须是一个子字符串，“pwke”是一个子序列，而不是子字符串。
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = range(len(s))
        left = 0
        v_i = {}
        ans = 0
        for index, value in enumerate(s):

            if value in v_i and v_i[value] >= left:
                left = v_i[value] + 1
            v_i[value] = index
            ans = max(ans, index - left + 1)

        return ans
