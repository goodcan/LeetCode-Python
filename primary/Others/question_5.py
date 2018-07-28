#!/usr/bin/env python
# @Time     : 2018/7/28 下午1:51
# @Author   : cancan
# @File     : question_5.py
# @Function : 有效的括号

"""
Question:
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
1.左括号必须用相同类型的右括号闭合。
2.左括号必须以正确的顺序闭合。

Note:
空字符串可被认为是有效字符串。

Example 1:
输入: "()"
输出: true

Example 2:
输入: "()[]{}"
输出: true

Example 3:
输入: "(]"
输出: false

Example 4:
输入: "([)]"
输出: false

Example 5:
输入: "{[]}"
输出: true
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True

        x = ['(', '{', '[']
        y = [')', '}', ']']
        z = ['()', '{}', '[]']
        r = []

        for i in s:
            if i in x:
                r.append(i)
            elif i in y:
                if not r: return False
                t = r.pop() + i
                if t not in z: return False

        return not r
