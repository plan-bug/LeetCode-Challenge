# 2 중 for 문
# 모든 요소끼리 차를 구한 후 그 중

from typing import List


class Solution:
    def maxProfit(self, prices) :
        if not prices:
            return 0
        p = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                p += prices[i] - prices[i-1]
        return p


solution = Solution()
print(solution.maxProfit([1, 2, 3, 4, 5]))
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
