#!/usr/bin/env python
# @Time     : 2018/5/27 下午12:57
# @Author   : cancan
# @File     : question_1.py
# @Function : 爬楼梯

"""
Question:
假设你正在爬楼梯。需要 n 步你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

Note:
给定 n 是一个正整数。

Example 1:
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 步 + 1 步
2.  2 步

Example 2:
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 步 + 1 步 + 1 步
2.  1 步 + 2 步
3.  2 步 + 1 步
"""


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        a = b = 1
        for _ in range(n - 1):
            a, b = b, a + b

        return b


if __name__ == "__main__":
    a = Solution()
    n = 6
    print(a.climbStairs(n))
