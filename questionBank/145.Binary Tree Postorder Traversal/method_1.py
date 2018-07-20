#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/20 17:29
# @Author   : cancan
# @File     : method_1.py
# @Function : 二叉树的后序遍历

"""
Question:
给定一个二叉树，返回它的 后序 遍历。

Example:
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [3,2,1]

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
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        r = []
        r.extend(self.postorderTraversal(root.left))
        r.extend(self.postorderTraversal(root.right))
        r.append(root.val)
        return r
