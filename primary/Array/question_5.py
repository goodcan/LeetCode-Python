#!/usr/bin/env python
# @Time     : 2018/5/1 下午7:13
# @Author   : cancan
# @File     : question_5.py
# @Function : 两个数组的交集 II

"""
Question:
给定两个数组，写一个方法来计算它们的交集。

Example:
给定 nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2, 2].

Note:
* 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
* 我们可以不考虑输出结果的顺序。

Follow up:
* 如果给定的数组已经排好序呢？你将如何优化你的算法？
* 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
* 如果nums2的元素存储在磁盘上，内存是有限的，你不能一次加载所有的元素到内存中，你该怎么办？
"""


class Solution1:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        ln1 = len(nums1)
        ln2 = len(nums2)
        a = {}
        r = []

        def foo(n1, n2):
            for i in n1:
                if i in a:
                    if i in n2[a[i]:]:
                        a[i] += n2[a[i]:].index(i) + 1
                        r.append(i)
                else:
                    if i in n2:
                        a[i] = n2.index(i) + 1
                        r.append(i)

        if ln1 <= ln2:
            foo(nums1, nums2)
        else:
            foo(nums2, nums1)

        return r


class Solution2:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        from collections import Counter

        return list((Counter(nums1) & Counter(nums2)).elements())


if __name__ == "__main__":
    s = Solution2()
    n1 = [3, 1, 2]
    n2 = [1, 1]
    print(s.intersect(n1, n2))
