#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/25 13:52
# @Author   : cancan
# @File     : question_1.py
# @Function : Fizz Buzz

"""
Question:
写一个程序，输出从 1 到 n 数字的字符串表示。
1.如果 n 是3的倍数，输出“Fizz”；
2.如果 n 是5的倍数，输出“Buzz”；
3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

Example：
n = 15,
返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""


class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        r = []

        for i in range(1, n + 1):
            if i % 3 == 0:
                if i % 5 == 0:
                    r.append('FizzBuzz')
                else:
                    r.append('Fizz')
            else:
                if i % 5 == 0:
                    r.append('Buzz')
                else:
                    r.append(str(i))

        return r
