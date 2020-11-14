# 컴프레션
# count 값이 N 인 요소 return
from typing import Collection, List

from collections import Counter


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        return [i[0] for i in Counter(A).items() if i[1] == len(A)/2][0]


solution = Solution()
print(solution.repeatedNTimes([3, 4, 3, 2]))
