#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-21 15:35
# @Author   : cancan
# @File     : method_1.py
# @Function : 二叉搜索树的范围和


"""
Question:
给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。
二叉搜索树保证具有唯一的值。

Example 1：
输入：root = [10,5,15,3,7,null,18], L = 7, R = 15
输出：32

Example 2：
输入：root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
输出：23

Note：
1. 树中的结点数量最多为 10000 个。
2. 最终的答案保证小于 2^31。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):

        temp = [root]
        ans = 0
        while temp:
            t = []

            for i in temp:
                if L <= i.val <= R:
                    ans += i.val

                if i.left:
                    t.append(i.left)

                if i.right:
                    t.append(i.right)

            temp = t

        return ans
