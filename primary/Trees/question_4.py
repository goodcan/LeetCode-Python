#!/usr/bin/env python
# @Time     : 2018/5/13 下午12:52
# @Author   : cancan
# @File     : question_4.py
# @Function : 二叉树的层次遍历

"""
Question:
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

Example:
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        r = [[root.val]]
        n = []
        t = []
        if root.left:
            t.append(root.left)
            n.append(root.left.val)
        if root.right:
            t.append(root.right)
            n.append(root.right.val)

        if n:
            r.append(n)

        while t:
            p = []
            n = []
            for i in t:
                if i.left:
                    p.append(i.left)
                    n.append(i.left.val)
                if i.right:
                    p.append(i.right)
                    n.append(i.right.val)
            if n:
                r.append(n)
            t = p

        return r
