# expression 으로 해결

from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        count = 0
        indices = [[j[i] for j in A]for i in range(len(A[0]))]
        for i in indices:
            if i != sorted(i):
                count += 1
        return count


solution = Solution()
print(solution.minDeletionSize(["zyx", "wvu", "tsr"]))
print(solution.minDeletionSize(["cba", "daf", "ghi"]))
