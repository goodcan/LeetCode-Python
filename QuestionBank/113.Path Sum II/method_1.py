#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-24 20:03
# @Author   : cancan
# @File     : method_1.py
# @Function : 路径总和 II


"""
Question:
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

Note: 叶子节点是指没有子节点的节点。

Example:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):

        self.ans = []

        if not root:
            return self.ans

        self.dfs(root, 0, [], sum)

        return self.ans

    def dfs(self, node, s, t, target):

        s += node.val
        t.append(node.val)

        if not node.left and not node.right:
            if s == target:
                self.ans.append(t.copy())
                return

        if node.left:
            self.dfs(node.left, s, t, target)
            t.pop()

        if node.right:
            self.dfs(node.right, s, t, target)
            t.pop()
