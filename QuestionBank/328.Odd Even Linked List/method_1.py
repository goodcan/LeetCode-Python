#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/27 14:24
# @Author   : cancan
# @File     : method_1.py
# @Function : 奇偶链表

"""
Question:
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，
这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

Example 1:
输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL

Example 2:
输入: 2->1->3->5->6->4->7->NULL
输出: 2->3->6->7->1->5->4->NULL

Note:
应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head):
        if not head:
            return head

        ret = head
        prev1 = head
        prev2 = None
        tmp = None
        flag = 1

        while 1:
            if flag % 2 != 0:
                if head.next is None:
                    head.next = tmp
                    if prev2:
                        prev2.next = None
                    break
                prev1 = head
            else:
                if tmp is None:
                    tmp = head

                if head.next is None:
                    if prev2:
                        prev2.next = head
                    prev1.next = tmp
                    break

                prev1.next = head.next

                if prev2:
                    prev2.next = head

                prev2 = head

            head = head.next
            flag += 1

        return ret
