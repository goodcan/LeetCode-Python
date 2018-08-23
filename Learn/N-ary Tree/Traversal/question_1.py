#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/2 16:09
# @Author   : cancan
# @File     : question_1.py
# @Function : N叉树的前序遍历

"""
Question:
给定一个N叉树，返回其节点值的前序遍历。

Example:
给定一个 3叉树 :
       1
     / | \
    3  2  4
   / \
  5   6
返回其前序遍历: [1,3,5,6,2,4]。

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
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []

        result = []

        def f(node, result):
            result.append(node.val)
            for item in node.children:
                f(item, result)

        f(root, result)

        return result
