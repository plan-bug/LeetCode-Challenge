# heapq 모듈 사용


import heapq


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int):
        heapq.heapify(A)
        for i in range(K):
            a = heapq.heappop(A)
            heapq.heappush(A, -a)
        return sum(A)
