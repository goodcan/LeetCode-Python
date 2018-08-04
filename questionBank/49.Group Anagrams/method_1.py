#!/usr/bin/env python
# @Time     : 2018/8/4 下午7:10
# @Author   : cancan
# @File     : method_1.py
# @Function : 字母异位词分组

"""
Question:
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

Example:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note
1.所有输入均为小写字母。
2.不考虑答案输出的顺序。
"""


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        t = {}

        for i in strs:
            s = ''.join(sorted(i))
            if s in t:
                t[s].append(i)
            else:
                t[s] = [i]

        return [i for i in t.values()]
