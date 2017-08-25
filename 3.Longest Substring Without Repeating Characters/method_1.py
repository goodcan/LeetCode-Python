#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Given a string, find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.

Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
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
