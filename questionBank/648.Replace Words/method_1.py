#!/usr/bin/env python
# @Time     : 2018/7/1 下午6:53
# @Author   : cancan
# @File     : method_1.py
# @Function : 单词替换

"""
Question:
在英语中，我们有一个叫做 词根(root)的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为
继承词(successor)。例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。
现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。
如果继承词有许多可以形成它的词根，则用最短的词根替换它。
你需要输出替换之后的句子。

Example:
输入: dict(词典) = ["cat", "bat", "rat"]
sentence(句子) = "the cattle was rattled by the battery"
输出: "the cat was rat by the bat"

Note:
1. 输入只包含小写字母。
2. 1 <= 字典单词数 <=1000
3. 1 <=  句中词语数 <= 1000
4. 1 <= 词根长度 <= 100
5. 1 <= 句中词语长度 <= 1000
"""


class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dict.sort(key=lambda x: len(x))
        s = sentence.split()
        for i, x in enumerate(s):
            for y in dict:
                if x.startswith(y):
                    s[i] = y
                    break

        return ' '.join(s)
