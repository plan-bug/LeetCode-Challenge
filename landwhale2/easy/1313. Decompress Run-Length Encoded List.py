class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        if len(nums) == 2:
            return [nums[1]] * nums[0]
        for i in range(0,len(nums)-1, 2):
            for j in range(nums[i]):
                result.append(nums[i+1])
        return result
