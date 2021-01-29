# 순간의 최선의 선택이 마지막엔 최선의 결과를 나타냄

# 위치를 정해야 하나? 아니면 매 순간 최선의 선택을 찾아야 하나

# 굳이 위치를 옮겨야 한다는 사고방식에 잡힐 필요 없음.
# 법칙성 찾아내는것이 포인트
# list 와 그에 따른 결과값의 상관관계를 찾는 것이 포인트

from typing import List


class Solution:
    def minCostToMoveChips(self, positions: List[int]) -> int:
        for i in positions:
            if i == 3:
                positions[i] = 2
        return [i-1 for i in positions if i == 3]


solution = Solution()
print(solution.minCostToMoveChips([2, 2, 2, 3, 3]))
