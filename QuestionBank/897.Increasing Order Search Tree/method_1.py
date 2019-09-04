#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/4 9:44
# @Author   : cancan
# @File     : method_1.py
# @Function : 递增顺序查找树

"""
Question:
给定一个树，按中序遍历重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。

Example:
输入：[5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9

Note:
给定树中的结点数介于 1 和 100 之间。
每个结点都有一个从 0 到 1000 范围内的唯一整数值。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        l = self.preorderTraversal(root)

        ret = TreeNode(l[0])
        tmp = ret
        for v in l[1:]:
            tmp.right = TreeNode(v)
            tmp = tmp.right

        return ret

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        r = []
        r.extend(self.preorderTraversal(root.left))
        r.append(root.val)
        r.extend(self.preorderTraversal(root.right))
        return r
