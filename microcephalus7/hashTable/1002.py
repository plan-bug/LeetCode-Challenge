# A의 요소 전부 튜플로 변형
# 모든 요소 더 한 list 생성
# list 에서 count 한 수에 3씩 나누어 몫 만큼 새로운 요소에 더함
from collections import Counter
from functools import reduce
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        return list(reduce(lambda x, y: x & y, [Counter(A[i]) for i in range(len(A))]).elements())


solution = Solution()
print(solution.commonChars(["bella", "label", "roller"]))
