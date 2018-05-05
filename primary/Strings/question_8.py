#!/usr/bin/env python
# @Time     : 2018/5/5 上午11:31
# @Author   : cancan
# @File     : question_8.py
# @Function : 数数并说

"""
Question:
报数序列是指一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
给定一个正整数 n ，输出报数序列的第 n 项。
注意：整数顺序将表示为一个字符串。

Example 1:
输入: 1
输出: "1"

Example 2:
输入: 4
输出: "1211"
"""


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        a = '1'
        for i in range(n - 1):
            t = []
            r = ''
            for y in a:
                if t and y not in t:
                    r += str(len(t)) + t[0]
                    t = []
                    t.append(y)
                else:
                    t.append(y)
            else:
                if t:
                    r += str(len(t)) + t[0]
            a = r
        else:
            return a

if __name__ == "__main__":
    a = Solution()
    for i in range(1, 7):
        print(str(i) + ': ', a.countAndSay(i))
    # print(a.countAndSay(5))
