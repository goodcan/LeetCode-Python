#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/5 18:24
# @Author   : cancan
# @File     : method_1.py
# @Function : 删除排序链表中的重复元素

"""
Question:
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

Example 1:
输入: 1->1->2
输出: 1->2

Example 2:
输入: 1->1->2->3->3
输出: 1->2->3
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        t = [head.val]
        prev_node = head
        next_node = head.next

        while next_node:
            if next_node.val in t:
                prev_node.next = next_node.next
                next_node = next_node.next
            else:
                t.append(next_node.val)
                prev_node = next_node
                next_node = next_node.next

        return head
