#!/usr/bin/env python
# @Time     : 2018/4/7 下午10:52
# @Author   : cancan
# @File     : method_1.py
# @Function : 旋转数据

"""
Question:
将包含 n 个元素的数组向右旋转 k 步。

Example:
如果n = 7,k = 3，给定数组[1,2,3,4,5,6,7]，向右旋转后的结果为[5,6,7,1,2,3,4]。

Note:
尽可能找到更多的解决方案，这里最少有三种不同的方法解决这个问题。
"""


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        nums[:k], nums[k: l] = nums[l-k: l], nums[: l-k]
