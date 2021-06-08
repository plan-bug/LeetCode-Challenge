# 1 을 어떻게 다룰 것이냐

# 필요 조건
# grid(2중 List) 개념 및 다루기
# 언제 row, column 의 전환할 것이냐

# 숙지 사항
# 0을 최대한 1로
# 1을 최대한 0로

# 방법
# row 돌며 0, 1 갯수 구한 후 변경 및 저장
# col 돌며 0, 1 갯수 구한 후 변경 및 저장
# row, col 비교하여 최댓값 return

from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        res = (1 << N - 1) * M

        for j in range(1, N):
            cur = sum(grid[i][j] == grid[i][0] for i in range(M))
            res += max(cur, M - cur) * (1 << N - 1 - j)
        return res
