#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/7 10:19
# @Author   : cancan
# @File     : method_1.py
# @Function : 另一个树的子树

"""
Question:
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

Example 1:
给定的树 s:
     3
    / \
   4   5
  / \
 1   2
给定的树 t：
   4
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

Example 2:
给定的树 s：
     3
    / \
   4   5
  / \
 1   2
    /
   0
给定的树 t：
   4
  / \
 1   2
返回 false。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        tmp = [s]

        while tmp:
            newTmp = []
            for i in tmp:
                if i.left:
                    newTmp.append(i.left)
                if i.right:
                    newTmp.append(i.right)

                if self.check(i, t):
                    return True
            tmp = newTmp
        return False

    def check(self, n1: TreeNode, n2: TreeNode) -> bool:
        if n1 is None and n2 is None:
            return True
        if not all([n1, n2]):
            return False
        if n1.val != n2.val:
            return False

        return self.check(n1.left, n2.left) and self.check(n1.right, n2.right)
