#!/usr/bin/env python
# @Time     : 2018/5/1 下午9:58
# @Author   : cancan
# @File     : question_9.py
# @Function : 两数之和

"""
Question:
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

Example:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution1:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i, v in enumerate(nums):
            d = target - v
            if d in nums:
                index = nums.index(d)
                if index != i:
                    return [i, index]


class Solution2:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        t = {}
        for i, v in enumerate(nums):
            d = target - v
            if d in t:
                return [t[d], i]
            else:
                t[v] = i


class Solution3:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        t = {}
        for i in range(len(nums)):
            d = target - nums[i]
            if d in t:
                return [t[d], i]
            else:
                t[nums[i]] = i


if __name__ == "__main__":
    s = Solution3()
    d = [3, 2, 4]
    t = 6
    print(s.twoSum(d, t))
