class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = sum(i%2==0 for i in position)
        return min(even, len(position)-even)
