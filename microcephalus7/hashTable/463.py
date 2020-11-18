# 2중 컴프리헨션
# i, j 로 나눠 i+1, i-1, j+1, j-1 이 1이냐 0이냐 에 따라 1씩 더한 수 생성

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column]:
                    res += 4
                    if row and grid[row-1][column]:
                        res -= 2
                    if column and grid[row][column-1]:
                        res -= 2
        return res


solution = Solution()
print(solution.islandPerimeter(
    [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
