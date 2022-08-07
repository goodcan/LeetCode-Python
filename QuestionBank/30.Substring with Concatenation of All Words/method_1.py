#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/8/7 11:49
# @Author   : cancan
# @File     : method_1.py
# @Function : 串联所有单词的子串

"""
给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。

示例 1：
输入：s = "barfoothefoobarman", words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。

示例 2：
输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
输出：[]

示例 3：
输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
输出：[6,9,12]

提示：
1 <= s.length <= 104
s 由小写英文字母组成
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] 由小写英文字母组成
"""

from typing import *


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        sl = len(s)
        words.sort()
        wl = len(words[0])
        wn = len(words)
        idx = 0
        ans = []
        while idx + wl * wn <= sl:
            tmp = []
            for i in range(wn):
                w = s[idx + wl * i:idx + wl * (i + 1)]
                if w not in words:
                    break
                tmp.append(w)

            tmp.sort()
            if tmp == words:
                ans.append(idx)

            idx += 1

        return ans
