#!/usr/bin/env python
# @Time     : 2018/5/3 下午9:54
# @Author   : cancan
# @File     : question_3.py
# @Function : 字符串中的第一个唯一字符

"""
Question:
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

Example:
s = "leetcode"
返回 0.
s = "loveleetcode",
返回 2.

Note:
您可以假定该字符串只包含小写字母。
"""

class Solution1:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i, v in enumerate(s):
            if v not in s[i+1:] + s[:i]:
                return i
        else:
            return -1

class Solution2:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = []
        for i, v in enumerate(s):
            if v in t:
                continue
            if v in s[i+1:]:
                t.append(v)
            else:
                return i
        else:
            return -1


class Solution3:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = list(set(s))
        i = [s.index(t) for t in l if s.count(t) == 1]
        return min(i) if i else -1


if __name__ == "__main__":
    a = Solution3()
    s = "leetcode"
    print(a.firstUniqChar(s))
