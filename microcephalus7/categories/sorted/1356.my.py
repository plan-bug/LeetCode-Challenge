# 먼저 정렬
# lambda 식으로 각 수들의 2진수에서 1의 갯수를 기준으로 정렬

from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(sorted(arr), key=lambda x: bin(x)[2:].count("1"))


solution = Solution()
print(solution.sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]))
print(solution.sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
print(solution.sortByBits([10000, 10000]))
print(solution.sortByBits([2, 3, 5, 7, 11, 13, 17, 19]))
print(solution.sortByBits([10, 100, 1000, 10000]))
