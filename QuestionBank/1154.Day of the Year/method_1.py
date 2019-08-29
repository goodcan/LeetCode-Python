#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/8/29 14:56
# @Author   : cancan
# @File     : method_1.py
# @Function : 一年中的第几天

"""
Question:
给你一个按 YYYY-MM-DD 格式表示日期的字符串 date，请你计算并返回该日期是当年的第几天。
通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。每个月的天数与现行公元纪年法（格里高利历）一致。

Example 1：
输入：date = "2019-01-09"
输出：9

Example 2：
输入：date = "2019-02-10"
输出：41

Example 3：
输入：date = "2003-03-01"
输出：60

Example 4：
输入：date = "2004-03-01"
输出：61

Note：
date.length == 10
date[4] == date[7] == '-'，其他的 date[i] 都是数字。
date 表示的范围从 1900 年 1 月 1 日至 2019 年 12 月 31 日
"""


class Solution:
    def dayOfYear(self, date: str) -> int:
        ds = date.split('-')
        year, month, day = int(ds[0]), int(ds[1]), int(ds[2])

        tmp = {
            1: 0,
            2: 31,
            3: 59,
            4: 90,
            5: 120,
            6: 151,
            7: 181,
            8: 212,
            9: 243,
            10: 273,
            11: 304,
            12: 334
        }

        ans = tmp[month] + day

        if self.isLeapYear(year) and month > 2:
            ans += 1

        return ans

    def isLeapYear(self, year: int) -> bool:
        if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
            return True
        return False
