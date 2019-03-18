#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-18 14:33
# @Author   : cancan
# @File     : method_1.py
# @Function : 平衡二叉树


"""
Question:
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
    一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

Example 1:
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true

Example 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):

        self.res = True

        self.bfs(root)

        return self.res

    def bfs(self, node: TreeNode):

        if node:
            hl = self.bfs(node.left)
            hr = self.bfs(node.right)

            if abs(hl - hr) > 1:
                self.res = False

            return max(hl, hr) + 1

        else:
            return 0
