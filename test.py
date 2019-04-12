#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/4/12 9:29
# @Author   : cancan
# @File     : test.py
# @Function :

class Solution:
    def reverseVowels(self, s: str) -> str:
        yy = {
            'a', 'e', 'i', 'o', 'u',
            'A', 'E', 'I', 'O', 'U'
        }

        s = list(s)

        r = 0
        l = len(s) - 1

        while l > r:
            if s[r] in yy and s[l] in yy:
                s[r], s[l] = s[l], s[r]
                r += 1
                l -= 1
            elif s[r] in yy and s[l] not in yy:
                l -= 1
            elif s[r] not in yy and s[l] in yy:
                r += 1
            else:
                r += 1
                l -= 1

        return ''.join(s)

s = Solution()
print(s.reverseVowels('race car'))
"race car"

