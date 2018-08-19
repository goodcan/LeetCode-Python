#!/usr/bin/env python
# @Time     : 2018/7/12 下午9:30
# @Author   : cancan
# @File     : question_2.py
# @Function : 排序链表

"""
Question:
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

Example 1:
输入: 4->2->1->3
输出: 1->2->3->4

Example 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        values = [head.val]
        t = head.next
        while t:
            values.append(t.val)
            t = t.next

        values.sort()
        r = ListNode(values[0])
        t = r
        for i in values[1:]:
            t.next = ListNode(i)
            t = t.next

        return r
