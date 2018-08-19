#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/6/29 10:17
# @Author   : cancan
# @File     : method_1.py
# @Function : 翻转二叉树

"""
Question:
翻转一棵二叉树。

Example:
输入：
     4
   /   \
  2     7
 / \   / \
1   3 6   9

输出：
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def f(node):
            if node:
                node.left, node.right = node.right, node.left
                f(node.left)
                f(node.right)
            else:
                return

        f(root)

        return root