class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        return sum(min(i,j) for i in map(max,grid) for j in map(max,zip(*grid))) - sum(map(sum,grid))