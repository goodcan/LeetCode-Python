#!/usr/bin/python
# -*- coding: utf-8 -*-

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
