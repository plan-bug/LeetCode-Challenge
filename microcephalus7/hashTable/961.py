# 컴프레션
# count 값이 N 인 요소 return
from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        A.sort()
        a = 0
        while(True):
            if A.count(A[a]) == len(A)/2:
                return A[a]
            a += 1


solution = Solution()
print(solution.repeatedNTimes([3, 4, 3, 2]))
