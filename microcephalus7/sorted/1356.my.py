# list 각 요소 ()로 묶음
# () 내부에는 원래 요소와 2진법 할 시 1의 개수
# 1의 개수를 기준으로 정렬

from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return [i for (i, j) in sorted([(i, bin(i)[2:].count('1'))
                                        for i in arr], key=lambda x: x[1])]


solution = Solution()
print(solution.sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]))
print(solution.sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
print(solution.sortByBits([10000, 10000]))
print(solution.sortByBits([2, 3, 5, 7, 11, 13, 17, 19]))
print(solution.sortByBits([10, 100, 1000, 10000]))
