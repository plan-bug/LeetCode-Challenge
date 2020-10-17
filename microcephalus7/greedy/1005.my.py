# for 문
# 횟수는 K
# A 안에 제일 작은 수 change
from typing import List


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int):
        for i in range(K):
            A[A.index(min(A))] = - A[A.index(min(A))]

        return sum(A)


solution = Solution()
print(solution.largestSumAfterKNegations([4, 2, 3], 1))
print(solution.largestSumAfterKNegations([3, -1, 0, 2], 3))
