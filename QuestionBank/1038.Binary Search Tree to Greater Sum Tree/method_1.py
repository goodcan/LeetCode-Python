#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/9/21 15:41
# @Author   : cancan
# @File     : method_1.py
# @Function : 从二叉搜索树到更大和树

"""
给出二叉 搜索 树的根节点，该二叉树的节点值各不相同，修改二叉树，使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
提醒一下，二叉搜索树满足下列约束条件：

节点的左子树仅包含键 小于 节点键的节点。
节点的右子树仅包含键 大于 节点键的节点。
左右子树也必须是二叉搜索树。

示例：
输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

提示：
树中的节点数介于 1 和 100 之间。
每个节点的值介于 0 和 100 之间。
给定的树为二叉搜索树。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
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
