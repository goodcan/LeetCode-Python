#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/7/8 17:34
# @Author   : cancan
# @File     : method_1.py
# @Function : IP 地址无效化

"""
Question:
给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。
所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。

Example 1：
输入：address = "1.1.1.1"
输出："1[.]1[.]1[.]1"

Example 2：
输入：address = "255.100.50.0"
输出："255[.]100[.]50[.]0"

Note：
给出的 address 是一个有效的 IPv4 地址
"""


class Solution:
    def defangIPaddr(self, address):
        return address.replace(".", "[.]")
