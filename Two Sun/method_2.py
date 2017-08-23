#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        result_dict = {}
        for i, t in enumerate(nums):
            if t in result_dict:
                return [result_dict[t], i]
            else:
                n = target - t
                result_dict[n] = i


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    target = 3
    solution = Solution()
    print solution.twoSum(nums,target)
