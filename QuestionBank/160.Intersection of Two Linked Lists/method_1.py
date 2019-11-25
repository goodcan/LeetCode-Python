#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-18 21:15
# @Author   : cancan
# @File     : method_1.py
# @Function : 相交链表


"""
Question:
编写一个程序，找到两个单链表相交的起始节点。

Example 1：
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

Example 2：
输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

Example 3：
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。

Note：
1.如果两个链表没有交点，返回 null.
2.在返回结果后，两个链表仍须保持原有的结构。
3.可假定整个链表结构中没有循环。
4.程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
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
