#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-21 12:50
# @Author   : cancan
# @File     : method_1.py
# @Function : 单值二叉树

"""
Question:
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
只有给定的树是单值二叉树时，才返回 true；否则返回 false。

Example 1：
输入：[1,1,1,1,1,null,1]
输出：true

Example 2：
输入：[2,2,2,5,2]
输出：false

Note：
* 给定树的节点数范围是 [1, 100]。
* 每个节点的值都是整数，范围为 [0, 99] 。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):

        if not root:
            return True

        a = root.val
        temp = [root]

        while temp:

            t = []

            for i in temp:
                if i.val != a:
                    return False

                if i.left:
                    t.append(i.left)

                if i.right:
                    t.append(i.right)

            temp = t

        return True
