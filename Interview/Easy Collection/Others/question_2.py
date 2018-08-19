#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/6/27 23:11
# @Author   : cancan
# @File     : question_2.py
# @Function : 汉明距离

"""
Question:
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
给出两个整数 x 和 y，计算它们之间的汉明距离。

Note:
0 ≤ x, y < 231.

Example:
输入: x = 1, y = 4
输出: 2
解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
上面的箭头指出了对应二进制位不同的位置。
"""


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        list_x = list(reversed(bin(x)[2:]))
        list_y = list(reversed(bin(y)[2:]))

        len_x = len(list_x)
        len_y = len(list_y)

        if len_x > len_y:
            count = self.get_count(len_x, list_x, list_y)
        else:
            count = self.get_count(len_y, list_y, list_x)

        return count

    def get_count(self, list_len, list_x, list_y):
        count = 0
        t = 0
        for i, v in enumerate(list_y):
            if list_x[i] != v:
                count += 1
            t = i
        if t + 1 < list_len:
            for ii in list_x[t + 1:]:
                if ii == '1':
                    count += 1

        return count


if __name__ == "__main__":
    s = Solution()
    print(s.hammingDistance(0, 10))
