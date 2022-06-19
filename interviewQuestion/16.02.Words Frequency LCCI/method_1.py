#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/6/17 10:50
# @Author   : cancan
# @File     : method_1.py
# @Function : 单词频率

"""
设计一个方法，找出任意指定单词在一本书中的出现频率。
你的实现应该支持如下操作：
WordsFrequency(book)构造函数，参数为字符串数组构成的一本书
get(word)查询指定单词在书中出现的频率

Example：
WordsFrequency wordsFrequency = new WordsFrequency({"i", "have", "an", "apple", "he", "have", "a", "pen"});
wordsFrequency.get("you"); //返回0，"you"没有出现过
wordsFrequency.get("have"); //返回2，"have"出现2次
wordsFrequency.get("an"); //返回1
wordsFrequency.get("apple"); //返回1
wordsFrequency.get("pen"); //返回1

Note：
- book[i]中只包含小写字母
- 1 <= book.length <= 100000
- 1 <= book[i].length <= 10
- get函数的调用次数不会超过100000
"""

from typing import List


class WordsFrequency:

    def __init__(self, book: List[str]):
        self.data = {}
        for v in book:
            self.data.setdefault(v, 0)
            self.data[v] += 1

    def get(self, word: str) -> int:
        return self.data.get(word, 0)

# Your WordsFrequency object will be instantiated and called as such:
# obj = WordsFrequency(book)
# param_1 = obj.get(word)
