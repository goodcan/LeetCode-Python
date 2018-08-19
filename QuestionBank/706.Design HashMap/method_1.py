#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/8/1 13:54
# @Author   : cancan
# @File     : method_1.py
# @Function : 设计哈希映射

"""
QQuestion:
不使用任何内建的哈希表库设计一个哈希映射
具体地说，你的设计应该包含以下的功能
1.put(key, value)：向哈希映射中插入(键,值)的数值对。如果键对应的值已经存在，更新这个值。
2.get(key)：返回给定的键所对应的值，如果映射中不包含这个键，返回-1。
3.remove(key)：如果映射中存在这个键，删除这个数值对。

Example
MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);
hashMap.put(2, 2);
hashMap.get(1);            // 返回 1
hashMap.get(3);            // 返回 -1 (未找到)
hashMap.put(2, 1);         // 更新已有的值
hashMap.get(2);            // 返回 1
hashMap.remove(2);         // 删除键为2的数据
hashMap.get(2);            // 返回 -1 (未找到)

Note
1.所有的值都在 [1, 1000000]的范围内。
2.操作的总数目在[1, 10000]范围内。
3.不要使用内建的哈希库。
"""


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def put(self, key, value):
        """
        value will always be positive.
        :type key: int
        :type value: int
        :rtype: void
        """
        self.d[key] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        return self.d.get(key, -1)

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        if key in self.d:
            del self.d[key]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
