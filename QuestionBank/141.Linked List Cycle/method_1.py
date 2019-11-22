#!/usr/bin/env python
# @Time     : 2018/5/5 下午7:44
# @Author   : cancan
# @File     : method_1.py
# @Function : 环形链表

"""
Question:
给定一个链表，判断链表中是否有环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

Example 1：
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

Example 2：
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。

Example 3：
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。

Follow up：
你能用 O(1)（即，常量）内存解决此问题吗？
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        # n1 每次走一步
        n1 = head.next

        # n2 每次走两步
        n2 = head.next.next

        while n2:
            # n2 走的比 n1 较快，如果有环则会追上 n1
            if n1 == n2:
                return True
            n1 = n1.next
            if n1:
                n2 = n2.next
                if n2:
                    n2 = n2.next
                else:
                    return False
            else:
                return False
        return False
