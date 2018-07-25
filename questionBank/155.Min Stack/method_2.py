#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/25 10:23
# @Author   : cancan
# @File     : method_2.py
# @Function : 最小栈

"""
Question:
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
1.push(x) -- 将元素 x 推入栈中。
2.pop() -- 删除栈顶的元素。
3.top() -- 获取栈顶元素。
g4.etMin() -- 检索栈中的最小元素。

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.t = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.t:
            self.t.append((x, x))
        else:
            self.t.append((x, min(x, self.t[-1][1])))

    def pop(self):
        """
        :rtype: void
        """
        self.t.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.t[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.t[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
