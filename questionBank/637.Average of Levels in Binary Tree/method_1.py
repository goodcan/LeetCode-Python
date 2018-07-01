#!/usr/bin/env python
# @Time     : 2018/7/1 下午12:16
# @Author   : cancan
# @File     : method_1.py
# @Function : 二叉树的层平均值

"""
Question:
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.

Example:
输入:
    3
   / \
  9  20
    /  \
   15   7
输出: [3, 14.5, 11]
解释:
第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].

Note:
节点值的范围在32位有符号整数范围内。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = [root.val]
        t = []
        if root.left:
            t.append(root.left)
        if root.right:
            t.append(root.right)

        while t:
            res.append(sum([_.val for _ in t]) / len(t))
            temp = []
            for _ in t:
                if _.left:
                    temp.append(_.left)
                if _.right:
                    temp.append(_.right)
            t = temp

        return res
