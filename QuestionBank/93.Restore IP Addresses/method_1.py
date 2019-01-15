#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-01-14 23:54
# @Author   : cancan
# @File     : method_1.py
# @Function : 复原IP地址

"""
Question:
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

Example:
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        self._calculate([], s, 4)
        return ['.'.join(i) for i in self.res]

    def _calculate(self, cur, s, n):
        l = len(s)

        if l == 0 and n == 0 and cur not in self.res:
            self.res.append(cur)

        if l == 0 or n < 0:
            return
        else:
            for i in range(1, 4):
                if self._is_0_to_255(s[:i]):
                    d = cur.copy()
                    d.append(s[:i])
                    self._calculate(d, s[i:], n - 1)

    def _is_0_to_255(self, s):

        i = int(s)
        l = len(s)

        if l > 0 and i > 0 and i <= 255 and s[0] != '0':
            return True
        elif l == 1 and i == 0:
            return True
        else:
            return False
