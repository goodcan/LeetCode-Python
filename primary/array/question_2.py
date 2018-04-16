#!/usr/bin/env python
# @Time     : 2018/4/10 下午10:22
# @Author   : cancan
# @File     : question_2.py
# @Function : 买卖股票的最佳时机


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        t = 0
        for i, v in enumerate(prices):
            next = i + 1
            if next < l and prices[next] > prices[i]:
                t += prices[next] - prices[i]

        return t

if __name__ == '__main__':
    t = Solution()
    a = [6,1,3,2,4,7]
    r = t.maxProfit(a)
    print(r)
