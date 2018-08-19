#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/16 15:42
# @Author   : cancan
# @File     : method_1.py
# @Function : N叉树的后序遍历

"""
Question:
给定一个N叉树，返回其节点值的后序遍历。

Example:
例如，给定一个 3叉树 :
       1
     / | \
    3  2  4
   / \
  5   6
返回其后序遍历: [5,6,3,2,4,1].

Note:
递归法很简单，你可以使用迭代法完成此题吗?
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []

        def f(node, data):
            if not node: return

            for item in node.children:
                f(item, data)

            data.append(node.val)

        f(root, result)

        return result
