class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        vals = sorted(i for i, j in points)
        return max(vals[i] - vals[i-1] for i in range(1, len(vals)))