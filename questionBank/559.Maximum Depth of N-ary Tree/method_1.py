#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/1 13:17
# @Author   : cancan
# @File     : method_1.py
# @Function : N叉树的最大深度

"""
Question:
给定一个N叉树，找到其最大深度。
最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
例如，给定一个 3叉树 :
     1
   / | \
  3  2  4
 / \
5   6
我们应返回其最大深度，3。

Note:
1.树的深度不会超过 1000。
2.树的节点总不会超过 5000。
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        count = 0
        if not root:
            return count
        else:
            t = [root]

        while t:
            count += 1
            temp = []

            for node in t:
                temp.extend(node.children)

            t = temp

        return count
