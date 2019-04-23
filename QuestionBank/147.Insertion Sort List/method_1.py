#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/4/23 17:53
# @Author   : cancan
# @File     : method_1.py
# @Function : 对链表进行插入排序


"""
Question:
对链表进行插入排序。

插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

插入排序算法：
插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。

Example 1：
输入: 4->2->1->3
输出: 1->2->3->4

Example 2：
输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):
        if not head:
            return None

        node = head
        temp = [node]

        while node.next:
            nextNode = node.next

            if node.val > nextNode.val:
                l = len(temp)
                i = l - 2

                while i >= 0 and temp[i].val > nextNode.val:
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

        return temp[0]
