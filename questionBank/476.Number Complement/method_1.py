#!/usr/bin/env python
# @Time     : 2018/6/24 上午12:15
# @Author   : cancan
# @File     : method_1.py
# @Function : 数字的补数

"""
Question:
给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。

Note:
1.给定的整数保证在32位带符号整数的范围内。
2.你可以假定二进制数不包含前导零位。

Example 1:
输入: 5
输出: 2
解释: 5的二进制表示为101（没有前导零位），其补数为010。所以你需要输出2。 5的二进

Example 2:
输入: 1
输出: 0
解释: 1的二进制表示为1（没有前导零位），其补数为0。所以你需要输出0。
"""


class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        b = bin(num)[2:]
        res = ''
        for i in b:
            if i == '1':
                res += '0'
            else:
                res += '1'

        return int(res, 2)
