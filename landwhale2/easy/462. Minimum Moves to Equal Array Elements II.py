class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        mid = len(nums) // 2
        midnum = nums_sorted[mid]
        res = 0
        for num in nums_sorted:
            res += abs(num - midnum)
        res = int(res)
        return res
