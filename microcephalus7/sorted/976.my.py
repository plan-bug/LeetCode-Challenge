# 정렬 후 iterable
# 3수 묶어서 삼각형 법칙에 맞을 경우 list 넣음
# list 비어 있을 시 return 0
# list 안 비었을 시 return 최대값

from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        array = [A[i]+A[i+1]+A[i+2]
                 for i in range(len(A)-2) if A[i+2] < (A[i+1] + A[i])]
        if array == []:
            return 0
        return max(array)


solution = Solution()
print(solution.largestPerimeter([3, 2, 3, 4]))

print(solution.largestPerimeter([1, 2, 1]))
print(solution.largestPerimeter([2, 1, 2]))
