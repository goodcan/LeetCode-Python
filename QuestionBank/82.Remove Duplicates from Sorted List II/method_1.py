#!/usr/bin/env python
# @Time     : 2018/7/15 下午2:58
# @Author   : cancan
# @File     : method_1.py
# @Function : 删除排序链表中的重复元素 II

"""
Question:
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

Example 1:
输入: 1->2->3->3->4->4->5
输出: 1->2->5

Example 2:
输入: 1->1->1->2->3
输出: 2->3
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
        t = {}
        prev = None
        node = head

        while node:
            if node.val not in t:
                t[node.val] = {'num': 1, 'node': prev}
            else:
                t[node.val]['num'] += 1

            prev = node
            if t[node.val]['num'] > 1:
                if t[node.val]['node']:
                    t[node.val]['node'].next = node.next
                    prev = t[node.val]['node']
                else:
                    prev = None
                    head = node.next

            node = node.next

        return head
