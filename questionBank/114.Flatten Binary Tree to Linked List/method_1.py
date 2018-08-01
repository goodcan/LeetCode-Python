#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/1 15:35
# @Author   : cancan
# @File     : method_1.py
# @Function : 二叉树展开为链表

"""
Question:
给定一个二叉树，原地将它展开为链表。

Example:
给定二叉树
    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        d = []

        def f(node):
            if not node:
                return

            d.append(node.val)
            f(node.left)
            f(node.right)

        f(root)

        t = root
        for i in d[1:]:
            t.right = TreeNode(i)
            t.left = None
            t = t.right
