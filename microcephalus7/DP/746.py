# dp list엔 이전 값들 저장 되고 매 연산마다 dp 값 참고

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        dp = [0] * len(cost)
        dp[0] = cost[0]
        if len(cost) >= 2:
            dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-1], dp[-2])


solution = Solution()
print(solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
