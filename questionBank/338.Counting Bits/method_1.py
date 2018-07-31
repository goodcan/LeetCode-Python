#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/31 15:20
# @Author   : cancan
# @File     : method_1.py
# @Function : Bit位计数

"""
Question:
给定一个非负整数 num。 对于范围 0 ≤ i ≤ num 中的每个数字 i ，计算其二进制数中的1的数目并将它们作为数组返回。

Example
比如给定 num = 5 ，应该返回 [0,1,1,2,1,2].

Follow up:
1.给出时间复杂度为O(n * sizeof(integer)) 的解答非常容易。 但是你可以在线性时间O(n)内用一次遍历做到吗？
2.要求算法的空间复杂度为O(n)。
3.你能进一步完善解法吗？ 在c ++或任何其他语言中不使用任何内置函数（如c++里的 __builtin_popcount）来执行此操作。

Credits：
特别感谢 @syedee 添加此问题及所有测试用例。
"""


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        r = []
        for i in range(num + 1):
            r.append(bin(i).count('1'))

        return r
