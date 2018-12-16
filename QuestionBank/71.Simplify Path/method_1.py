#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018-12-16 22:12
# @Author   : cancan
# @File     : method_1.py
# @Function : 简化路径

"""
Question:
给定一个文档 (Unix-style) 的完全路径，请进行路径简化。

Example:
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Note:
1.你是否考虑了 路径 = "/../" 的情况？
  在这种情况下，你需返回 "/" 。
2.此外，路径中也可能包含多个斜杠 '/' ，如 "/home//foo/" 。
  在这种情况下，你可忽略多余的斜杠，返回 "/home/foo" 。
"""


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_list = path.strip('/').split('/')
        r = []
        for i in path_list:
            if not i or i == '.':
                continue
            elif i == '..':
                if r and r[-1] != i:
                    r.pop()
            else:
                r.append(i)

        return '/' + '/'.join(r)
