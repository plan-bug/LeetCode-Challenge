class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum([len([j for j in i if j < 0]) for i in grid])