#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/2 10:28
# @Author   : cancan
# @File     : method_1.py
# @Function : 二叉树的层次遍历 II

"""
Question:
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

Example
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []

        r = []
        t = [root]

        while t:
            r.insert(0, [i.val for i in t])

            temp = []
            for i in t:
                if i.left: temp.append(i.left)
                if i.right: temp.append(i.right)

            t = temp

        return r
