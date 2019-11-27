#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/11/27 11:10
# @Author   : cancan
# @File     : method_1.py
# @Function : 旋转链表

"""
Question:
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

Example 1:
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL

Example 2:
输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0:
            return head

        tmp = []
        oldHead = head

        while head:
            tmp.append(head)
            head = head.next

        l = len(tmp)
        if l == 0:
            return oldHead
        if k >= l:
            k = k % l
            if k == 0:
                return oldHead

        oldLast = tmp[-1]
        newLast = tmp[-(k + 1)]
        newLast.next = None
        oldLast.next = oldHead

        return tmp[-k]
