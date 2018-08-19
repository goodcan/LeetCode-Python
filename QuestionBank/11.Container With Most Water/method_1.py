#!/usr/bin/python

"""
Question:
给定n个非负整数，a1,a2，…an，每个表示坐标(i,ai)的点。
画出两条直线，即(i,ai)和(i,0)的两个端点，找到两条直线，
与x轴组成一个容器，求出最多能装多少水。

Note:
您不能倾斜容器，n至少是2。
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        ans = 0
        left = 0
        l = len(height)
        right = l - 1
        while left < right:
            a = height[left]
            b = height[right]
            temp = min(a, b) * (right - left)
            if temp > ans:
                ans = temp
            if a > b:
                right -= 1
            else:
                left += 1

        return ans
