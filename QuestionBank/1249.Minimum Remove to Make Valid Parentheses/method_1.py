#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/11/7 9:59
# @Author   : cancan
# @File     : method_1.py
# @Function : 移除无效的括号


"""
Question:
给你一个由 '('、')' 和小写字母组成的字符串 s。
你需要从字符串中删除最少数目的 '(' 或者 ')' （可以删除任意位置的括号)，使得剩下的「括号字符串」有效。
请返回任意一个合法字符串。
有效「括号字符串」应当符合以下 任意一条 要求：
空字符串或只包含小写字母的字符串
可以被写作 AB（A 连接 B）的字符串，其中 A 和 B 都是有效「括号字符串」
可以被写作 (A) 的字符串，其中 A 是一个有效的「括号字符串」

Example 1：
输入：s = "lee(t(c)o)de)"
输出："lee(t(c)o)de"
解释："lee(t(co)de)" , "lee(t(c)ode)" 也是一个可行答案。

Example 2：
输入：s = "a)b(c)d"
输出："ab(c)d"

Example 3：
输入：s = "))(("
输出：""
解释：空字符串也是有效的

Example 4：
输入：s = "(a(b(c)d)"
输出："a(b(c)d)"
 
Note：
1 <= s.length <= 10^5
s[i] 可能是 '('、')' 或英文小写字母
在真实的面试中遇到过这道题？
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        tmpIndex = []
        ret = ''
        delNum = 0
        for i, v in enumerate(s):
            if v == '(':
                tmpIndex.append(i - delNum)
            elif v == ')':
                if len(tmpIndex) <= 0:
                    delNum += 1
                    continue
                else:
                    tmpIndex.pop()
            ret += v

        if len(tmpIndex) > 0:
            lastNum = 0
            for i in tmpIndex:
                ret = ret[:i - lastNum] + ret[i + 1 - lastNum:]
                lastNum += 1

        return ret
