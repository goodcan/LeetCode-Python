#!/usr/bin/env python
# @Time     : 2018/5/6 下午5:13
# @Author   : cancan
# @File     : question_1.py
# @Function : 二叉树的最大深度

"""
Question:
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

Note:
叶子节点是指没有子节点的节点。

Example:
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        n = 1
        t = []
        if root.left:
            t.append(root.left)
        if root.right:
            t.append(root.right)

        while t:
            n += 1
            p = []
            for i in t:
                if i.left:
                    p.append(i.left)
                if i.right:
                    p.append(i.right)
            t = p

        return n


if __name__ == "__main__":
    a = Solution()
    root = stringToTreeNode('[3,9,20,null,null,15,7]')
    print(a.maxDepth(root))
