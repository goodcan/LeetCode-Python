#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/9/24 10:19
# @Author   : cancan
# @File     : method_1.py
# @Function : 二叉搜索树中的众数


"""
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：
- 结点左子树中所含结点的值小于等于当前结点的值
- 结点右子树中所含结点的值大于等于当前结点的值
- 左子树和右子树都是二叉搜索树

例如：
给定 BST [1,null,2,2],
   1
    \
     2
    /
   2
返回[2].

提示：如果众数超过1个，不需考虑输出顺序
进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        data = {root.val: 1}
        countMax = 1
        tmp = [root]

        while len(tmp) > 0:
            newTmp = []
            for node in tmp:
                if node.left:
                    newTmp.append(node.left)
                    data.setdefault(node.left.val, 0)
                    data[node.left.val] += 1
                    if data[node.left.val] > countMax:
                        countMax = data[node.left.val]

                if node.right:
                    newTmp.append(node.right)
                    data.setdefault(node.right.val, 0)
                    data[node.right.val] += 1
                    if data[node.right.val] > countMax:
                        countMax = data[node.right.val]

            tmp = newTmp

        ret = []
        for k, v in data.items():
            if v == countMax:
                ret.append(k)

        ret = sorted(ret)

        return ret
