#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-18 21:15
# @Author   : cancan
# @File     : method_1.py
# @Function : 相交链表


"""
Question:
编写一个程序，找到两个单链表相交的起始节点。
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        listA = self.get_list(headA)
        listB = self.get_list(headB)

        lenA = len(listA)
        lenB = len(listB)

        if listA[-1] != listB[-1]:
            return None

        if lenA > lenB:
            l = lenB - 1
        else:
            l = lenA - 1

        for i in range(l):
            if listB[lenB - i - 2] != listA[lenA - i - 2]:
                return listB[lenB - i - 1]

        if lenA > lenB:
            return listB[0]
        else:
            return listA[0]

    def get_list(self, head):

        l = [head]

        while head.next:
            l.append(head.next)
            head = head.next

        return l
