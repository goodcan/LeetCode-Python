#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Question:
给定一个不同的数字集合，返回所有可能的排列。

Example:
[1,2,3] 有如下排列:
    [
        [1,2,3],
        [1,3,2],
        [2,1,3],
        [2,3,1],
        [3,1,2],
        [3,2,1]
    ]
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        if nums is None:
            return ans
        if len(nums) == 0:
            ans.append([])
        for each in nums:
            temp = nums[:]        # 复制nums列表
            temp.remove(each)
            for i in self.permute(temp):
                i.insert(0, each)
                ans.append(i)
        return ans

a = [1, 2, 3]
b = Solution()
print b.permute(a)