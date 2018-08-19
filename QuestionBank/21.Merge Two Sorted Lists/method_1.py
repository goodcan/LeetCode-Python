#!/usr/bin/env python
# @Time     : 2018/5/5 下午5:34
# @Author   : cancan
# @File     : method_1.py
# @Function : 合并两个有序链表

"""
Question:
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

Example:
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1

        t = [l1, l2]

        n = l1.next
        while n:
            t.append(n)
            n = n.next

        n = l2.next
        while n:
            t.append(n)
            n = n.next

        t = sorted(t, key=lambda x: x.val)

        r = t[0]
        p = r

        for i in t:
            p.next = i
            p = i
        else:
            p.next = None

        return r
