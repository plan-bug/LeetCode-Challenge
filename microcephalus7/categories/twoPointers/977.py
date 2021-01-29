# compression

from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([i ** 2 for i in A])


solution = Solution()
print(solution.sortedSquares([-4, -1, 0, 3, 10]))
