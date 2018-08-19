#!/usr/bin/env python
# @Time     : 2018/5/27 下午2:50
# @Author   : cancan
# @File     : question_3.py
# @Function : 最大子序和

"""
Question:
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

Example:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

Follow up:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = nums[0]
        s = 0
        for _ in nums:
            s = max(s + _, _)
            r = max(r, s)
        return r


if __name__ == "__main__":
    a = Solution()
    n = [1, 2, -1]
    print(a.maxSubArray(n))