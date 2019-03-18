#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-18 15:47
# @Author   : cancan
# @File     : method_1.py
# @Function : 路径总和


"""
Question:
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，
这条路径上所有节点值相加等于目标和。
说明: 叶子节点是指没有子节点的节点。

Example:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        return self.dfs(root, 0, sum)

    def dfs(self, node: TreeNode, s: int, sum: int):

        if not node:
            return False

        s += node.val

        l = self.dfs(node.left, s, sum)
        r = self.dfs(node.right, s, sum)

        if not node.left and not node.right:
            return s == sum
        else:
            return l or r
