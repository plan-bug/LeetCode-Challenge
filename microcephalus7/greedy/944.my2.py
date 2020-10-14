# 사전 list 화 없이 바로 expression

from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        count = 0
        for j in range(len(A[0])):
            indice = [i[j] for i in A]
            if indice != sorted(indice):
                count += 1
        return count


solution = Solution()
print(solution.minDeletionSize(["zyx", "wvu", "tsr"]))
print(solution.minDeletionSize(["cba", "daf", "ghi"]))
