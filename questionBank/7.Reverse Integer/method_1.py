#!/usr/bin/python

"""
Question:
整数的反向数字。

Example1: x = 123, return 321
Example2: x = -123, return -321

Note:
输入假定为一个32位的带符号整数。
当反向的整数溢出时，函数应该返回0。
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        x = x
        if x >= 0:
            x = reversed(str(x))
            t = ''
            for i in x:
                t += i

            r = int(t)
            if r > (2 ** 31 - 1):
                return 0
            else:
                return r

        else:
            x = reversed(str(0 - x))
            t = ''
            for i in x:
                t += i

            r = int(t)
            if r > (2 ** 31 - 1):
                return 0
            else:
                return 0 - r