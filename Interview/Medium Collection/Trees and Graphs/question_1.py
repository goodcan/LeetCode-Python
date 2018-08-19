#!/usr/bin/env python
# @Time     : 2018/8/5 下午3:10
# @Author   : cancan
# @File     : question_1.py
# @Function : 中序遍历二叉树

"""
Question:
给定一个二叉树，返回它的中序 遍历。

Example:
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [1,3,2]

Follow up:
递归算法很简单，你可以通过迭代算法完成吗？
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        r = []
        r.extend(self.inorderTraversal(root.left))
        r.append(root.val)
        r.extend(self.inorderTraversal(root.right))
        return r
