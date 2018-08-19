#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/20 14:18
# @Author   : cancan
# @File     : method_1.py
# @Function : 二叉树的中序遍历

"""
Question:
给定一个二叉树，返回它的中序 遍历。

Example:
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [1,3,2]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.r = []
        self.traverse(root)
        return self.r

    def traverse(self, node):
        if not node:
            return
        self.traverse(node.left)
        self.r.append(node.val)
        self.traverse(node.right)