#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-15 16:33
# @Author   : cancan
# @File     : method_1.py
# @Function : 数据流的中位数


"""
Question:
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

Example：
[2,3,4] 的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：
    * void addNum(int num) - 从数据流中添加一个整数到数据结构中。
    * double findMedian() - 返回目前所有元素的中位数。

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2

Follow up:
1.如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
2.如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
"""


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.t = []

    def addNum(self, num):

        if not self.t:
            self.t.append(num)
            return

        for i, v in enumerate(self.t):
            if v > num:
                self.t.insert(i, num)
                return

        self.t.append(num)

    def findMedian(self):
        l = len(self.t)

        if l % 2:
            return self.t[l // 2] * 1.0
        else:
            d = l // 2
            return (self.t[d - 1] + self.t[d]) * 1.0 / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
