#!/usr/bin/env python
# @Time     : 2018/5/5 下午7:44
# @Author   : cancan
# @File     : method_1.py
# @Function : 环形链表

"""
Question:
给定一个链表，判断链表中是否有环。

Follow up:
你能否不使用额外空间解决此题？
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        # n1 每次走一步
        n1 = head.next

        # n2 每次走两步
        n2 = head.next.next

        while n2:
            # n2 走的比 n1 较快，如果有环则会追上 n1
            if n1 == n2:
                return True
            n1 = n1.next
            if n1:
                n2 = n2.next
                if n2:
                    n2 = n2.next
                else:
                    return False
            else:
                return False
        return False
