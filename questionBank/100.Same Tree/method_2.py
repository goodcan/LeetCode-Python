#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/24 10:23
# @Author   : cancan
# @File     : method_2.py
# @Function : 相同的树

"""
Question:
给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

Example 1:
输入:       1         1
          / \       / \
         2   3     2   3
        [1,2,3],   [1,2,3]
输出: true

Example 2:
输入:      1          1
          /           \
         2             2
        [1,2],     [1,null,2]
输出: false

Example 3:
输入:       1         1
          / \       / \
         2   1     1   2
        [1,2,1],   [1,1,2]
输出: false
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return (p == None and q == None) or \
               (p != None and
                q != None and
                p.val == q.val and
                self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
