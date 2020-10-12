#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/10/12 15:43
# @Author   : cancan
# @File     : method_1.py
# @Function : 二叉搜索树的最小绝对差

"""
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

示例：
输入：

   1
    \
     3
    /
   2
输出：
1

解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.ans = -1
        self.pre = -1
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        if self.pre != -1 and self.ans == -1:
            self.ans = node.val - self.pre
        elif node.val - self.pre < self.ans:
            self.ans = node.val - self.pre
        self.pre = node.val
        self.dfs(node.right)
