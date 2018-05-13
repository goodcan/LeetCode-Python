#!/usr/bin/env python
# @Time     : 2018/5/13 下午3:04
# @Author   : cancan
# @File     : method_1.py
# @Function : 合并两个有序数组

"""
Question:
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

Note:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

Example:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        d = m - 1
        for i in nums2:
            for y in range(d + 1):
                if i >= nums1[d - y]:
                    nums1[d - y + 1] = i
                    d += 1
                    break
                else:
                    nums1[d - y + 1], nums1[d - y] = \
                        nums1[d - y], nums1[d - y + 1]
                    if d - y == 0:
                        nums1[0] = i
                        d += 1
                        break
