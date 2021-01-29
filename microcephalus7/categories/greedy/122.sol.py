# 차익 이득이 날 때마다 바로 파는 시스템.
# 그리디에 따라 for 문을 돌면서 해당 날짜의 시세와 전날의 시세에서 이득이 생기면 바로 팜 (탐욕 선택 속성)
# 마지막 까지 고려했을 때도 차익의 합이 최고값이므로 이득.

# 3, 2, ,9, 10 이 있을 경우
# 3을 고려하지 않아도 됨
# 그 다음 날 바로 더 낮아지므로 떨어진 만큼 차익이 생김
# 10 도 고려하지 않아도 됨
# 2 에서 10에 파는 것이 이득이겠지만
# 9에서 팔아도
# 9에서 사고 10에서 팔면 그만큼 차익을 채울 수 있기 때문에 팜

from typing import List


class Solution:
    def maxProfit(self, prices):
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
