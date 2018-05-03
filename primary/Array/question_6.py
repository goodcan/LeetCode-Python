#!/usr/bin/env python
# @Time     : 2018/5/1 下午9:01
# @Author   : cancan
# @File     : question_6.py
# @Function : 加一

"""
Question:
给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。
最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

Example 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

Example 2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
"""


class Solution1:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s1 = ''
        for i in digits:
            s1 += str(i)

        s1 = str(int(s1) + 1)

        r = []

        for i in s1:
            r.append(int(i))

        return r


class Solution2:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i, v in enumerate(digits):
            num = num * 10 + digits[i]
        s = str(num + 1)
        return [int(i) for i in s]


if __name__ == "__main__":
    s = Solution1()
    d = [1, 2, 3]
    print(s.plusOne(d))
