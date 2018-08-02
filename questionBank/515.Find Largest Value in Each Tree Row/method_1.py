#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/2 10:41
# @Author   : cancan
# @File     : method_1.py
# @Function : 在每个树行中找最大值

"""
Question:
您需要在二叉树的每一行中找到最大的值。

Example
输入:
      1
     / \
    3   2
   / \   \
  5   3   9
输出: [1, 3, 9]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []

        r = []
        t = [root]

        while t:
            d = None
            temp = []
            for i in t:
                d = max(i.val, d)
                if i.left: temp.append(i.left)
                if i.right: temp.append(i.right)
            r.append(d)
            t = temp

        return r
