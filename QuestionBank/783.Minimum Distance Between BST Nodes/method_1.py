#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/10/12 15:48
# @Author   : cancan
# @File     : method_1.py
# @Function : 二叉搜索树节点最小距离

"""
给定一个二叉搜索树的根节点 root，返回树中任意两节点的差的最小值。

示例：
输入: root = [4,2,6,1,3,null,null]
输出: 1
解释:
注意，root是树节点对象(TreeNode object)，而不是数组。

给定的树 [4,2,6,1,3,null,null] 可表示为下图:

          4
        /   \
      2      6
     / \
    1   3

最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。

注意：
1.二叉树的大小范围在 2 到 100。
2.二叉树总是有效的，每个节点的值都是整数，且不重复。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
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
