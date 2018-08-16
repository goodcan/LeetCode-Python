#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/16 18:10
# @Author   : cancan
# @File     : method_1.py
# @Function : 删除链表中的节点

"""
Question:
删除链表中等于给定值 val 的所有节点。

Example:
输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        r = head
        prev = None
        while head:
            if head.val == val:
                if prev:
                    prev.next = head.next
                    head = head.next
                else:
                    r = head.next
                    head.next = None
                    head = r
            else:
                prev = head
                head = head.next

        return r
