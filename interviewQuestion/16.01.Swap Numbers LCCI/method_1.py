#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/7/15 21:34
# @Author   : cancan
# @File     : method_1.py
# @Function : 交换数字

"""
Question:
编写一个函数，不用临时变量，直接交换numbers = [a, b]中a与b的值。

Example：
输入: numbers = [1,2]
输出: [2,1]

Note：
    numbers.length == 2
"""

from typing import List


class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0], numbers[1] = numbers[1], numbers[0]
        return numbers
