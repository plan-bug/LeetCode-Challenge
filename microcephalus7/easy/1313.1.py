class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return sum([nums[i]*[nums[i+1]] for i in range(0,len(nums),2)],[])