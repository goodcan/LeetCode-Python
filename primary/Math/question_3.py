#!/usr/bin/env python
# @Time     : 2018/7/15 下午1:44
# @Author   : cancan
# @File     : question_3.py
# @Function : 3的幂

"""
Question:
给定一个整数，写一个函数来判断它是否是 3 的幂次方。

Example 1:
输入: 27
输出: true

Example 2:
输入: 0
输出: false

Example 3:
输入: 9
输出: true

Example 4:
输入: 45
输出: false

Follow up:
你能不使用循环或者递归来完成本题吗？
"""


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while True:
            if n == 1:
                return True
            if n % 3 == 0:
                n = n // 3
            else:
                return False
