#!/usr/bin/env python
# @Time     : 2018/5/5 下午1:53
# @Author   : cancan
# @File     : method_1.py
# @Function : 删除链表的倒数第N个节点

"""
Question:
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

Example:
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.

Note:
给定的 n 保证是有效的。

Follow up:
你能尝试使用一趟扫描实现吗？
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next:
            return None
        nodes = [head]
        t = head.next
        while t:
            nodes.append(t)
            t = t.next
        if n == 1:
            nodes[-2].next = None
        else:
            nodes[-n].val = nodes[-n].next.val
            nodes[-n].next = nodes[-n].next.next

        return head
