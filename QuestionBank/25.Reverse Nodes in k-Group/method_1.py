#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/16 21:12
# @Author   : cancan
# @File     : method_1.py
# @Function : K 个一组翻转链表

"""
Question:
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

Example：
给你这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5

Note：
1.你的算法只能使用常数的额外空间。
2.你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        count = 0
        tmp = head
        ret = head
        end = None
        while head:
            count += 1
            head = head.next
            if count % k == 0:
                lastEnd = end
                start, end = self.reversedSomeListNode(tmp, k)
                if count / k == 1:
                    ret = start
                else:
                    lastEnd.next = start
                tmp = head
                end.next = head

        return ret

    def reversedSomeListNode(self, head: ListNode, k: int) -> (ListNode, ListNode):
        pre = head
        next = head.next
        head.next = None
        n = 1
        while next:
            tmp = next.next
            next.next = pre
            pre = next
            n += 1
            if n == k:
                return pre, head
            next = tmp
