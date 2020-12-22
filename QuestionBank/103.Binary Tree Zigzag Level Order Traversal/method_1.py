#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/12/22 10:01
# @Author   : cancan
# @File     : method_1.py
# @Function : 二叉树的锯齿形层序遍历

"""
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层序遍历如下：
[
  [3],
  [20,9],
  [15,7]
]
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []

        if not root:
            return ans

        flag = 1
        tmp = [root]

        while len(tmp) > 0:
            newTmp = []
            ansTmp = []

            for node in tmp:
                if flag == 1:
                    ansTmp.append(node.val)
                else:
                    ansTmp.insert(0, node.val)

                if node.left:
                    newTmp.append(node.left)

                if node.right:
                    newTmp.append(node.right)

            flag = 2 if flag == 1 else 1
            ans.append(ansTmp)
            tmp = newTmp

        return ans
