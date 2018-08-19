#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/26 11:27
# @Author   : cancan
# @File     : question_3.py
# @Function : 颠倒二进制位

"""
Question:
颠倒给定的 32 位无符号整数的二进制位。

Example:
输入: 43261596
输出: 964176192
解释: 43261596 的二进制表示形式为 00000010100101000001111010011100 ，
     返回 964176192，其二进制表示形式为 00111001011110000010100101000000 。

Follow up:
如果多次调用这个函数，你将如何优化你的算法？
"""


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int('{0:032}'.format(int(bin(n)[2:]))[::-1], 2)
