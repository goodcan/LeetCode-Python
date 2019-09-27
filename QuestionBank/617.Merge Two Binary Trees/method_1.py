#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/27 9:59
# @Author   : cancan
# @File     : method_1.py
# @Function : 合并二叉树

"""
Question:
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，
否则不为 NULL 的节点将直接作为新二叉树的节点。

Example 1:
输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7

Note: 合并必须从两个树的根节点开始。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None:
            return t2
        if t2 == None:
            return t1

        self.dfs(t1, t2)

        return t1

    def dfs(self, node1, node2):

        node1.val += node2.val

        if node2.left != None:
            if node1.left == None:
                node1.left = node2.left
            else:
                self.dfs(node1.left, node2.left)

        if node2.right != None:
            if node1.right == None:
                node1.right = node2.right
            else:
                self.dfs(node1.right, node2.right)
