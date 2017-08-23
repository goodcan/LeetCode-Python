#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums_len_list = range(len(nums))
        for i in nums_len_list:
            n = target - nums[i]
            if (nums.count(n) != 0) and (nums.index(n) != i):
                return [i, nums.index(n)]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    target = 3
    solution = Solution()
    print solution.twoSum(nums,target)
