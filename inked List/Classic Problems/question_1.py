#!/usr/bin/env python
# @Time     : 2018/5/5 下午3:06
# @Author   : cancan
# @File     : question_1.py
# @Function : 反转链表

"""
Question:
反转一个单链表。

Example:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

Follow up:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        def f(node, pre):
            t = node.next
            node.next = pre
            if not t:
                return node
            else:
                return f(t, node)

        return f(head, None)
