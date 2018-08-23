#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/23 11:58
# @Author   : cancan
# @File     : question_2.py
# @Function : 至少是其他数字两倍的最大数

"""
Question:
在一个给定的数组nums中，总是存在一个最大元素 。
查找数组中的最大元素是否至少是数组中每个其他数字的两倍。
如果是，则返回最大元素的索引，否则返回-1。

Example 1:
输入: nums = [3, 6, 1, 0]
输出: 1
解释: 6是最大的整数, 对于数组中的其他整数,
6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.

Example 2:
输入: nums = [1, 2, 3, 4]
输出: -1
解释: 4没有超过3的两倍大, 所以我们返回 -1.

Note:
1.nums 的长度范围在[1, 50].
2.每个 nums[i] 的整数范围在 [0, 99].
"""


class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        index = nums.index(m)
        del nums[index]

        for i in nums:
            if m < 2 * i:
                return -1

        return index
