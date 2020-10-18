# heapq 모듈 사용
# A 의 가장 작은 수 return
# - 로 변환하여 list 에 push

import heapq
from typing import List


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int):
        heapq.heapify(A)
        for i in range(K):
            a = heapq.heappop(A)
            heapq.heappush(A, -a)
        return sum(A)
