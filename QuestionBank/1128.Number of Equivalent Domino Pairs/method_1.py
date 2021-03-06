#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/8/27 15:37
# @Author   : cancan
# @File     : method_1.py
# @Function : 等价多米诺骨牌对的数量

"""
Question:
给你一个由一些多米诺骨牌组成的列表 dominoes。
如果其中某一张多米诺骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。
形式上，dominoes[i] = [a, b] 和 dominoes[j] = [c, d] 等价的前提是 a==c 且 b==d，或是 a==d 且 b==c。
在 0 <= i < j < dominoes.length 的前提下，找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i, j) 的数量。

Example：
输入：dominoes = [[1,2],[2,1],[3,4],[5,6]]
输出：1
 
Note：
1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9
"""

from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        tmp = {}
        ans = 0

        for v in dominoes:
            if (v[0], v[1]) in tmp:
                tmp[(v[0], v[1])] += 1
            elif (v[1], v[0]) in tmp:
                tmp[(v[1], v[0])] += 1
            else:
                tmp[tuple(v)] = 1

        for v in tmp.values():
            if v == 1:
                continue

            ans += int(self.factorial(v) / (self.factorial(2) * self.factorial((v - 2))))

        return ans

    def factorial(self, num):
        ret = 1

        for v in range(2, num + 1):
            ret *= v

        return ret
