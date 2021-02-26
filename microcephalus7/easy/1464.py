class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return eval('*'.join([str(i-1) for i in sorted(nums)[-2:]]))
        