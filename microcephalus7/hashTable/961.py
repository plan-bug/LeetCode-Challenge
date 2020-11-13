# 컴프레션
# count 값이 N 인 요소 return
from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        return [i for i in A if A.count(i) == (len(A)/2)][0]


solution = Solution()
print(solution.repeatedNTimes([3, 4, 3, 2]))
