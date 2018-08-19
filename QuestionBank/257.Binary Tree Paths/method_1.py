#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/1 13:40
# @Author   : cancan
# @File     : method_1.py
# @Function : 二叉树的所有路径

"""
Question:
给定一个二叉树，返回所有从根节点到叶子节点的路径。
说明: 叶子节点是指没有子节点的节点。

Example:
输入:
   1
 /   \
2     3
 \
  5
输出: ["1->2->5", "1->3"]
解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        r = []

        def f(node, l, prev=None):
            if prev and not prev.left and not prev.right:
                r.append('->'.join(l))

            if not node:
                return

            l.append(str(node.val))
            f(node.left, l.copy(), node)
            f(node.right, l.copy(), node)

        f(root, [])

        return list(set(r))
