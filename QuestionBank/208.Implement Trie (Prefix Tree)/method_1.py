#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-03-11 22:59
# @Author   : cancan
# @File     : method_1.py
# @Function : 实现 Trie (前缀树)

'''
Question:
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

Example:
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true

Note:
1.你可以假设所有的输入都是由小写字母 a-z 构成的。
2.保证所有输入均为非空字符串。
'''


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = set()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.t.add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        return word in self.t

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        for item in self.t:
            if item.startswith(prefix):
                return True

        return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
