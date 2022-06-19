#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/6/17 10:30
# @Author   : cancan
# @File     : method_1.py
# @Function : 交换链表中的节点

"""
给你链表的头节点 head 和一个整数 k 。
交换 链表正数第 k 个节点和倒数第 k 个节点的值后，返回链表的头节点（链表 从 1 开始索引）。

Example 1：
输入：head = [1,2,3,4,5], k = 2
输出：[1,4,3,2,5]

Example 2：
输入：head = [7,9,6,6,7,8,3,0,9,5], k = 5
输出：[7,9,6,6,8,7,3,0,9,5]

Example 3：
输入：head = [1], k = 1
输出：[1]

Example 4：
输入：head = [1,2], k = 1
输出：[2,1]

Example 5：
输入：head = [1,2,3], k = 2
输出：[1,2,3]

Note：
- 链表中节点的数目是 n
- 1 <= k <= n <= 105
- 0 <= Node.val <= 100
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = [head]
        node = head
        while node.next:
            nodes.append(node.next)
            node = node.next

        l = len(nodes)
        if k > (l + 1) // 2:
            k = l - k + 1
        n1 = nodes[k - 1]
        n2 = nodes[-k]
        if n1 == n2:
            return head
        p1 = nodes[k - 2] if k - 2 >= 0 else None
        p2 = nodes[-k - 1] if k < l else None
        if n1.next == n2:
            n1.next, n2.next = n2.next, n1
            if p1:
                p1.next = n2
        else:
            n1.next, n2.next = n2.next, n1.next
            if p1:
                p1.next = n2
            if p2:
                p2.next = n1

        return n2 if k == 1 else head
