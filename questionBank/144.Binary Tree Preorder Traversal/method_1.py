#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/20 17:33
# @Author   : cancan
# @File     : method_1.py
# @Function : 二叉树的前序遍历

"""
Question:
给定一个二叉树，返回它的 前序 遍历。

Example:
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [1,2,3]

Follow up:
递归算法很简单，你可以通过迭代算法完成吗？
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        r = []
        r.append(root.val)
        r.extend(self.preorderTraversal(root.left))
        r.extend(self.preorderTraversal(root.right))
        return r
