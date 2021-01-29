# 변수 할당 참조.

class Solution:
    def minCostToMoveChips(self, positions: List[int]) -> int:
        odd, even = 0, 0
        for i in positions:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(even, odd)
