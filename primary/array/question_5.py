#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/4/17 9:42
# @Author   : cancan
# @File     : question_5.py
# @Function : 只出现一次的数字


class Solution1:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        c = Counter(nums)
        return c.most_common()[-1][0]


class Solution2:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        for i in nums:
            r ^= i

        return r


if __name__ == "__main__":
    a = Solution2()
    b = [1, 2, 2, 3, 4, 3, 4]
    r = a.singleNumber(b)
    print(r)
