#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/9/13 00:24
# @Author   : cancan
# @File     : method_1.py
# @Function : 单词搜索

"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false

提示：
board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.maxH = len(board)
        self.maxW = len(board[0])
        self.maxLen = len(word)

        for i in range(self.maxH):
            for j in range(self.maxW):
                key = "%s-%s" % (i, j)
                if self.dfs(0, i, j, {key: True}):
                    return True

        return False

    def dfs(self, idx, i, j, tmp):
        if i < 0 or i >= self.maxH or j < 0 or j >= self.maxW or self.board[i][j] != self.word[idx]:
            return False

        idx += 1
        if idx >= self.maxLen:
            return True

        key = "%s-%s" % (i, j + 1)
        if key not in tmp:
            tmp[key] = True
            if self.dfs(idx, i, j + 1, tmp):
                return True
            del tmp[key]

        key = "%s-%s" % (i, j - 1)
        if key not in tmp:
            tmp[key] = True
            if self.dfs(idx, i, j - 1, tmp):
                return True
            del tmp[key]

        key = "%s-%s" % (i + 1, j)
        if key not in tmp:
            tmp[key] = True
            if self.dfs(idx, i + 1, j, tmp):
                return True
            del tmp[key]

        key = "%s-%s" % (i - 1, j)
        if key not in tmp:
            tmp[key] = True
            if self.dfs(idx, i - 1, j, tmp):
                return True
            del tmp[key]

        return False
