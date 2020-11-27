# 외부에서 배열 생성
# 이터러블
# 이터러블 된 수 제외
# 해당 수 보다 작은 배열 생성
# =

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        profit = 0
        buyStock = prices[0]
        for i in range(len(prices)):
            if buyStock > prices[i]:
                buyStock = prices[i]
            profit = max((prices[i] - buyStock, profit))

        return profit


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
