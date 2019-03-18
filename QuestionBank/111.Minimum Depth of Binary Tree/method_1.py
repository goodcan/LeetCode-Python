#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-18 15:36
# @Author   : cancan
# @File     : method_1.py
# @Function : 二叉树的最小深度


"""
Question:
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

Note: 叶子节点是指没有子节点的节点。

Example:
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        h = 1
        temp = [root]

        while temp:
            t = []
            for i in temp:

                if not i.left and not i.right:
                    return h

                if i.left:
                    t.append(i.left)

                if i.right:
                    t.append(i.right)

            h += 1
            temp = t

        return h
