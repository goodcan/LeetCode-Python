#!/usr/bin/env python
# @Time     : 2018/5/5 下午7:28
# @Author   : cancan
# @File     : method_1.py
# @Function : 回文链表

"""
Question:
请检查一个链表是否为回文链表。

Follow up:
你能在 O(n) 的时间和 O(1) 的额外空间中做到吗
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        t = [head.val]
        n = head.next
        while n:
            t.append(n.val)
            n = n.next

        l = len(t)
        i = l // 2
        if l % 2 == 0:
            return t[:i] == t[i:][::-1]
        else:
            return t[:i] == t[i + 1:][::-1]
