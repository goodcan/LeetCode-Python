#!/usr/bin/env python
# @Time     : 2018/4/7 下午10:26
# @Author   : cancan
# @File     : question_3.py
# @Function : 旋转数组

class Solution1:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a = list(reversed(nums))
        for _ in range(k):
            b = a[0]
            del a[0]
            a.append(b)

        nums.clear()
        nums.extend(list(reversed(a)))


class Solution2:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        nums[:k], nums[k: l] = nums[l-k: l], nums[: l-k]
