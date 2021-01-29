# 이익 변수 생성 후 0 할당(이익의 마이너스 값 고려)
# 구입 변수 생성 후 첫번째 prices 에 생성
# 이터러블
# i가 구입변수보다 작을 시 구입 변수로 재 설정
# i-구입변수와 이익 비교해서 큰 수가 이익변수
# 이익변수 return

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        profit = 0
        buyStock = prices[0]
        for i in prices:
            if buyStock > i:
                buyStock = i
            profit = max((i - buyStock, profit))

        return profit


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
