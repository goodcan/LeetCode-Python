#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/4/24 18:42
# @Author   : cancan
# @File     : tt.py
# @Function : 


class Solution:
    def findLengthOfLCIS(self, nums):
        l = len(nums)

        if l in [0, 1]:
            return l

        start = 0
        end = 1
        ans = end - start

        while end < l:
            if nums[end] <= nums[end - 1]:
                if end - start > ans:
                    ans = end - start

                start = end
                end = start + 1

            else:
                end += 1

        if end - start > ans:
            ans = end - start

        return ans


s = Solution()
print(s.findLengthOfLCIS([1, 3, 5, 7]))
print(s.findLengthOfLCIS([2, 2, 2, 2, 2]))
print(s.findLengthOfLCIS([2, 2, 3, 1, 2]))
