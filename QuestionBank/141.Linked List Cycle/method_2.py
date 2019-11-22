#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/11/22 10:47
# @Author   : cancan
# @File     : method_2.py
# @Function : 环形链表

"""
Question:
给定一个链表，判断链表中是否有环。

Follow up:
你能否不使用额外空间解决此题？
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        tmp = {}
        while head:
            if head in tmp:
                return True
            else:
                tmp[head] = head
                head = head.next
        return False

