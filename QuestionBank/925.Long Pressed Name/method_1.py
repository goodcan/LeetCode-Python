#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/10/21 21:40
# @Author   : cancan
# @File     : method_1.py
# @Function : 长按键入

"""
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。

示例 1：
输入：name = "alex", typed = "aaleex"
输出：true
解释：'alex' 中的 'a' 和 'e' 被长按。

示例 2：
输入：name = "saeed", typed = "ssaaedd"
输出：false
解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。

示例 3：
输入：name = "leelee", typed = "lleeelee"
输出：true

示例 4：
输入：name = "laiden", typed = "laiden"
输出：true
解释：长按名字中的字符并不是必要的。

提示：
1.name.length <= 1000
2.typed.length <= 1000
3.name 和 typed 的字符都是小写字母。
"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        s1 = 0
        s2 = 0
        l1 = len(name)
        l2 = len(typed)
        while s1 < l1 and s2 < l2:
            if name[s1] == typed[s2]:
                s1 += 1
                s2 += 1
            else:
                if s2 == 0:
                    return False
                while s2 < l2 and typed[s2] == typed[s2 - 1]:
                    s2 += 1
                if s2 < l2 and name[s1] == typed[s2]:
                    s1 += 1
                    s2 += 1
                else:
                    return False

        if s1 < l1:
            return False

        while s2 < l2:
            if typed[s2] == typed[s2 - 1]:
                s2 += 1
            else:
                return False

        return True
