#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-21 11:46
# @Author   : cancan
# @File     : method_1.py
# @Function : 二叉树的堂兄弟节点


"""
Question:
在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
如果二叉树的两个节点深度相同，但父节点不同，则它们是一对堂兄弟节点。
我们给出了具有唯一值的二叉树的根节点 root，以及树中两个不同节点的值 x 和 y。
只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true。否则，返回 false。

Example 1：
输入：root = [1,2,3,4], x = 4, y = 3
输出：false

Example 2：
输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
输出：true

Example 3：
输入：root = [1,2,3,null,4], x = 2, y = 3
输出：false

Note：
* 二叉树的节点数介于 2 到 100 之间。
* 每个节点的值都是唯一的、范围为 1 到 100 的整数。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root, x, y):

        if not root:
            return False

        temp = [(None, root)]

        while temp:

            t = []
            has_x = None
            has_y = None

            for i in temp:
                prev = i[0]
                curr = i[1]
                if curr.val == x:
                    has_x = prev

                if curr.val == y:
                    has_y = prev

                if curr.left:
                    t.append((curr, curr.left))

                if curr.right:
                    t.append((curr, curr.right))

            if has_x and has_y and has_x != has_y:
                return True
            elif not has_x and not has_y:
                temp = t
            else:
                return False

        return False
