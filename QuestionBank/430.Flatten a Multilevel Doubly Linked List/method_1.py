#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/11/27 10:00
# @Author   : cancan
# @File     : method_1.py
# @Function : 扁平化多级双向链表

"""
Question:
您将获得一个双向链表，除了下一个和前一个指针之外，它还有一个子指针，可能指向单独的双向链表。
这些子列表可能有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。
扁平化列表，使所有结点出现在单级双链表中。您将获得列表第一级的头部。

Example:
输入:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
输出:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
"""


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Node) -> Node:
        self.dfs(head)
        return head

    def dfs(self, node):
        while node:
            if node.child:
                childLast = self.dfs(node.child)
                childLast.next = node.next
                if node.next:
                    node.next.prev = childLast
                node.next = node.child
                node.child.prev = node
                node.child = None
                if not childLast.next:
                    return childLast
                node = childLast.next
            else:
                if not node.next:
                    return node
                node = node.next
