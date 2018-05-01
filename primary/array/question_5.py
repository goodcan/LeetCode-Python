#!/usr/bin/env python
# @Time     : 2018/5/1 下午7:13
# @Author   : cancan
# @File     : question_5.py
# @Function : 两个数组的交集 II

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
