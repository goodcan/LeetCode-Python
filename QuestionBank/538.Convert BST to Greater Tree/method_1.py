#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/9/21 15:13
# @Author   : cancan
# @File     : method_1.py
# @Function : 把二叉搜索树转换为累加树

"""
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

例如：
输入: 原始二叉搜索树:
          5
        /   \
       2     13

输出: 转换为累加树:
         18
        /   \
      20     13
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        l = self.dfs(root)

        if len(l) <= 1:
            return root

        s = l[0].val
        for idx in range(1, len(l)):
            s += l[idx].val
            l[idx].val = s

        return root

    def dfs(self, root):
        if root is None:
            return []
        r = []
        r.extend(self.dfs(root.right))
        r.append(root)
        r.extend(self.dfs(root.left))
        return r