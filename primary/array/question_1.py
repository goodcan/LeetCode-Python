#!/usr/bin/env python
# @Time     : 2018/4/7 下午9:30
# @Author   : cancan
# @File     : question_1.py
# @Function : 从排序数组中删除重复项

class Solution1:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = []
        d = []
        for i, v in enumerate(nums):
            if v not in a:
                a.append(v)
            else:
                d.append(i)

        for _ in sorted(d, reverse=True):
           del nums[_]

        return len(nums)

class Solution2:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums.copy()
        nums.clear()
        nums.extend(sorted(list(set(a)), reverse=False))
        return len(nums)

if __name__ == '__main__':
    a = [-1, 0, 0, 3, 3]
    s = Solution2()
    print(s.removeDuplicates(a))
    print(a)
