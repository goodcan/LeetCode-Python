#!/usr/bin/env python
# @Time     : 2018/6/30 下午2:37
# @Author   : cancan
# @File     : method_1.py
# @Function : 检测大写字母

"""
Question:
给定一个单词，你需要判断单词的大写使用是否正确。
我们定义，在以下情况时，单词的大写用法是正确的：
 1.全部字母都是大写，比如"USA"。
 2.单词中所有字母都不是大写，比如"leetcode"。
 3.如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
否则，我们定义这个单词没有正确使用大写字母。

Example 1:
输入: "USA"
输出: True

Example 2:
输入: "FlaG"
输出: False

Note:
输入是由大写和小写拉丁字母组成的非空单词。
"""

class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word[0].isupper():
            for v in word[1:]:
                if v.isupper():
                    return False
            return True
        else:
            upper_count = 1
            for v in word[1:]:
                if v.isupper():
                    upper_count += 1

            if upper_count == 1:
                return True
            elif upper_count == len(word):
                return True
            else:
                return False

