#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/24 10:23
# @Author   : cancan
# @File     : method_1.py
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
        if p and q:
            t1 = [p]
            t2 = [q]
        elif not p and not q:
            return True
        else:
            return False

        while t1:

            tt1 = []
            tt2 = []

            for i, v in enumerate(t1):

                if t2[i].val != v.val:
                    return False

                if v.left and t2[i].left:
                    tt1.append(v.left)
                    tt2.append(t2[i].left)
                elif not v.left and not t2[i].left:
                    pass
                else:
                    return False

                if v.right and t2[i].right:
                    tt1.append(v.right)
                    tt2.append(t2[i].right)
                elif not v.right and not t2[i].right:
                    pass
                else:
                    return False

            t1 = tt1
            t2 = tt2

        return True
