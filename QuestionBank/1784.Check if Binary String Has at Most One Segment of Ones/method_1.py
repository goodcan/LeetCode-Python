#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/5/7 10:01
# @Author   : cancan
# @File     : method_1.py
# @Function : 查二进制字符串字段

"""
给你一个二进制字符串 s ，该字符串 不含前导零 。
如果 s 包含 零个或一个由连续的 '1' 组成的字段 ，返回 true​​​ 。否则，返回 false 。

Example 1：
输入：s = "1001"
输出：false
解释：字符串中的 1 没有形成一个连续字段。

Example 2：
输入：s = "110"
输出：true
 
Note：
 - 1 <= s.length <= 100
 - s[i]​​​​ 为 '0' 或 '1'
 - s[0] 为 '1'
"""


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        idx1 = -1
        for idx, v in enumerate(s):
            if v == '1':
                if idx == -1:
                    idx1 = idx
                else:
                    if idx - idx1 != 1:
                        return False
                    else:
                        idx1 = idx

        return True
