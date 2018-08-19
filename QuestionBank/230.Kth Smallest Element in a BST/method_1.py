#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/16 16:48
# @Author   : cancan
# @File     : method_1.py
# @Function : 二叉搜索树中第K小的元素

"""
Question:
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

Note:
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

Example 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1

Example 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3

Follow up:
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root: return None

        n = []
        t = [root]

        while t:
            temp = []
            for i in t:
                n.append(i.val)

                if i.left: temp.append(i.left)
                if i.right: temp.append(i.right)
            t = temp

        n.sort()

        return n[k - 1]
