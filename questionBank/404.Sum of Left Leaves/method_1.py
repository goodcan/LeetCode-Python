#!/usr/bin/env python
# @Time     : 2018/7/14 上午11:17
# @Author   : cancan
# @File     : method_1.py
# @Function : 左叶子之和

"""
Question:
计算给定二叉树的所有左叶子之和。

Example：
    3
   / \
  9  20
    /  \
   15   7
在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        r = 0
        t = [root]

        while t:
            temp = []
            for node in t:
                if node.left:
                    if not node.left.left and not node.left.right:
                        r += node.left.val
                    else:
                        temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            t = temp

        return r
