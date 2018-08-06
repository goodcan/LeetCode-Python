#!/usr/bin/env python
# @Time     : 2018/8/6 下午10:42
# @Author   : cancan
# @File     : method_1.py
# @Function : 填充同一层的兄弟节点

"""
Question:
给定一个二叉树
struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，
则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。

Note:
1.你只能使用额外常数空间。
2.使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
3.你可以假设它是一个完美二叉树（即所有叶子节点都在同一层，每个父节点都有两个子节点）。

Example:
给定完美二叉树，
     1
   /  \
  2    3
 / \  / \
4  5  6  7
调用你的函数后，该完美二叉树变为：
     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
"""


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        t = [root]

        while t:
            temp = []

            for i in range(len(t) - 1):
                t[i].next = t[i + 1]
                if t[i].left:
                    temp.append(t[i].left)
                if t[i].right:
                    temp.append(t[i].right)

            t[-1].next = None
            if t[-1].left:
                temp.append(t[-1].left)
            if t[-1].right:
                temp.append(t[-1].right)

            t = temp
