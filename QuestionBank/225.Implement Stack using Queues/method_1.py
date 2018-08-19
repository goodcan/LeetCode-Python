#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/24 11:38
# @Author   : cancan
# @File     : method_1.py
# @Function : 用队列实现栈

"""
Question:
使用队列实现栈的下列操作：
1.push(x) -- 元素 x 入栈
2.pop() -- 移除栈顶元素
3.top() -- 获取栈顶元素
4.empty() -- 返回栈是否为空

Note:
你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
"""


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.t.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.t.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.t[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.t

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
