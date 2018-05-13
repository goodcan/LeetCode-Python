#!/usr/bin/env python
# @Time     : 2018/5/13 下午1:07
# @Author   : cancan
# @File     : question_5.py
# @Function : 将有序数组转换为二叉搜索树

"""
Question:
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

Example:
给定有序数组: [-10,-3,0,5,9],
一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        def f(node, n):
            l = len(n)
            if l == 1:
                node.val = n[0]
                return
            d = l // 2
            node.val = n[d]
            if n[:d]:
                node.left = TreeNode(0)
                f(node.left, n[:d])
            if n[d + 1:]:
                node.right = TreeNode(0)
                f(node.right, n[d + 1:])

        r = TreeNode(0)
        f(r, nums)
        return r


class Solution2(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.createTrees(nums, 0, len(nums) - 1)

    def createTrees(self, n, left, right):
        if left > right:
            return
        mid = left + (right - left) // 2
        node = TreeNode(n[mid])
        node.left = self.createTrees(n, left, mid - 1)
        node.right = self.createTrees(n, mid + 1, right)
        return node


if __name__ == "__main__":
    a = Solution2()
    n = [-10, -3, 0, 5, 9]
    a.sortedArrayToBST(n)
