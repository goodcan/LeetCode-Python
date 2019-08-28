#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/8/28 10:29
# @Author   : cancan
# @File     : method_1.py
# @Function : 最大层内元素和

"""
Question:
给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。
请你找出层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。

Example
    1
   / \
  7   0
 / \
7  -8
输入：[1,7,0,7,-8,null,null]
输出：2
解释：
第 1 层各元素之和为 1，
第 2 层各元素之和为 7 + 0 = 7，
第 3 层各元素之和为 7 + -8 = -1，
所以我们返回第 2 层的层号，它的层内元素之和最大。

Note：
树中的节点数介于 1 和 10^4 之间
-10^5 <= node.val <= 10^5
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        node = root

        if not node:
            return 0

        maxLevel = 1
        maxSum = node.val

        level = 1
        tmp1 = [node]

        while tmp1:
            tmp2 = []
            level += 1
            s = 0

            for v in tmp1:
                if v.left:
                    tmp2.append(v.left)
                    s += v.left.val
                if v.right:
                    tmp2.append(v.right)
                    s += v.right.val

            if s > maxSum:
                maxLevel = level
                maxSum = s

            tmp1 = tmp2

        return maxLevel
