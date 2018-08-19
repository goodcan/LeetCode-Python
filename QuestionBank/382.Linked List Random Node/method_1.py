#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/2 10:53
# @Author   : cancan
# @File     : method_1.py
# @Function : 链表随机节点

"""
Question:
给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点被选的概率一样。

Follow up:
如果链表十分大且长度未知，如何解决这个问题？你能否使用常数级空间复杂度实现？

Example:
// 初始化一个单链表 [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom()方法应随机返回1,2,3中的一个，保证每个元素被返回的概率相等。
solution.getRandom();
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from random import sample


class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.t, temp = [], head
        while temp:
            self.t.append(temp)
            temp = temp.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        return sample(self.t, 1)[0].val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
