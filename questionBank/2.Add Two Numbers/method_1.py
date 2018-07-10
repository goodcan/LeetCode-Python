#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/10 11:40
# @Author   : cancan
# @File     : method_1.py
# @Function :


"""
Question:
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。
将两数相加返回一个新的链表。你可以假设除了数字 0 之外，这两个数字都不会以零开头。

Example：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def f(node):
            num = 0
            d = 0
            t = node
            while t:
                num += t.val * 10 ** d
                d += 1
                t = t.next

            return num

        num = str(f(l1) + f(l2))
        r = ListNode(int(num[-1]))
        t = r
        for i in num[:-1][::-1]:
            t.next = ListNode(int(i))
            t = t.next

        return r
