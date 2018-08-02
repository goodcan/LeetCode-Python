#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/2 10:18
# @Author   : cancan
# @File     : method_1.py
# @Function : N叉树的层序遍历

"""
Question:
给定一个N叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

例如，给定一个 3叉树 :
     1
   / | \
  3  2  4
 / \
5   6

返回其层序遍历:
[
    [1],
    [3,2,4],
    [5,6]
]

Note:
1.树的深度不会超过 1000。
2.树的节点总数不会超过 5000。
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        r = []
        t = [root]

        while t:
            r.append([i.val for i in t])

            temp = []
            for i in t:
                for j in i.children:
                    temp.append(j)

            t = temp

        return r
