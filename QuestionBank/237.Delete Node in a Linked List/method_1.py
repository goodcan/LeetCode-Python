#!/usr/bin/env python
# @Time     : 2018/5/5 下午1:30
# @Author   : cancan
# @File     : method_1.py
# @Function : 删除链表的结点

"""
Question:
请编写一个函数，使其可以删除某个链表中给定的（非末尾的）节点，您将只被给予要求被删除的节点。
比如：假设该链表为 1 -> 2 -> 3 -> 4  ，给定您的为该链表中值为 3 的第三个节点，
那么在调用了您的函数之后，该链表则应变成 1 -> 2 -> 4 。
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
