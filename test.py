#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/4/23 16:39
# @Author   : cancan
# @File     : test.py
# @Function : 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:

        node = head
        temp = [node]

        while node.next:
            nextNode = node.next

            if node.val > nextNode.val:
                l = len(temp)
                i = l - 2

                while i > 0 and temp[i].val > nextNode.val:
                    i -= 1

                i += 1

                node.next = nextNode.next

                nextNode.next = temp[i]

                if i > 0:
                    temp[i - 1].next = nextNode

                temp.insert(i, nextNode)
            else:
                temp.append(nextNode)
                node = nextNode

        return temp[0] if temp else None
