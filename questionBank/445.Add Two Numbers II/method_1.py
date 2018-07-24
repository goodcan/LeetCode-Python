#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/24 15:19
# @Author   : cancan
# @File     : method_1.py
# @Function : 两数相加 II

"""
Question:
给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。
它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。

Follow up
如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

Example:
输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出: 7 -> 8 -> 0 -> 7
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
        num = str(self.get_num(l1) + self.get_num(l2))
        r = ListNode(int(num[0]))
        t = r
        for i in num[1:]:
            t.next = ListNode(int(i))
            t = t.next
        return r

    def get_num(self, node):
        """
        推导链表对应整数
        :param node:
        :return:
        """
        num = 0
        t = node
        while t:
            num = num * 10 + t.val
            t = t.next
        return num
