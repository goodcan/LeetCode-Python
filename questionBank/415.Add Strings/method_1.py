#!/usr/bin/env python
# @Time     : 2018/7/14 上午11:25
# @Author   : cancan
# @File     : method_1.py
# @Function : 字符串相加

"""
Question:
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

Note
1.num1 和num2 的长度都小于 5100.
2.num1 和num2 都只包含数字 0-9.
3.num1 和num2 都不包含任何前导零。
4.你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) + int(num2))
