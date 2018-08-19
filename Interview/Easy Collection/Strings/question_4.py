#!/usr/bin/env python
# @Time     : 2018/5/3 下午11:25
# @Author   : cancan
# @File     : question_4.py
# @Function : 有效的字母异位词

"""
Question:
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

Example:
s = "anagram"，t = "nagaram"，返回 true
s = "rat"，t = "car"，返回 false

Note:
假定字符串只包含小写字母。

Follow up:
输入的字符串包含 unicode 字符怎么办？你能能否调整你的解法来适应这种情况？
"""

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if set(s) != set(t) or len(s) != len(t):
            return False

        for i, v in enumerate(s):
            if v == t[i]:
                continue

            elif v not in t:
                return False

            else:
                c_s = s.count(v)
                c_t = t.count(v)

                if c_s != c_t:
                    return False
                else:
                    return True
        else:
            return True


if __name__ == "__main__":
    a = Solution()
    s = ""
    t = ""
    print(a.isAnagram(s, t))