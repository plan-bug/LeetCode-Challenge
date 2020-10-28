# 정렬이 우선
# 다음 이터레이터로 전 요소와 지금 요소의 차이 구함
# 차이 값이 달라질 시 False
# 안 달라질 시 True
from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        formerNum = arr.pop(0)
        for i in sorted(arr):
            prog = i - formerNum


solution = Solution()
print(solution.canMakeArithmeticProgression([1, 3, 5]))
