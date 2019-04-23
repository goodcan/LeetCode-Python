#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/4/23 14:38
# @Author   : cancan
# @File     : method_1.py
# @Function : 比较含退格的字符串

"""
Question:
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。


Example 1：
输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。

Example 2：
输入：S = "ab##", T = "c#d#"
输出：true
解释：S 和 T 都会变成 “”。

Example 3：
输入：S = "a##c", T = "#a#c"
输出：true
解释：S 和 T 都会变成 “c”。

Example 4：
输入：S = "a#c", T = "b"
输出：false
解释：S 会变成 “c”，但 T 仍然是 “b”。

Note：
1 <= S.length <= 200
1 <= T.length <= 200
S 和 T 只含有小写字母以及字符 '#'。
"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        sl = len(S)
        tl = len(T)
        ss = ''
        tt = ''

        index = 0

        while 1:
            if index > sl and index > tl:
                break
            if index < sl:
                if S[index] == '#':
                    if ss:
                        ss = ss[:-1]
                else:
                    ss += S[index]
            if index < tl:
                if T[index] == '#':
                    if tt:
                        tt = tt[:-1]
                else:
                    tt += T[index]

            index += 1

        return ss == tt
