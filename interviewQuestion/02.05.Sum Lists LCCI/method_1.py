#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/12/3 19:52
# @Author   : cancan
# @File     : method_1.py
# @Function : 链表求和

"""
给定两个用链表表示的整数，每个节点包含一个数位。
这些数位是反向存放的，也就是个位排在链表首部。
编写函数对这两个整数求和，并用链表形式返回结果。

示例：
输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
输出：2 -> 1 -> 9，即912
进阶：思考一下，假设这些数位是正向存放的，又该如何解决呢?

示例：
输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
输出：9 -> 1 -> 2，即912
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        startTmp = ListNode(0)
        pre = startTmp
        add = 0

        while l1 or l2:
            tmp = add

            if l1:
                tmp += l1.val
                l1 = l1.next

            if l2:
                tmp += l2.val
                l2 = l2.next

            add = tmp // 10
            pre.next = ListNode(tmp % 10)
            pre = pre.next

        if add != 0:
            pre.next = ListNode(add)

        return startTmp.next
