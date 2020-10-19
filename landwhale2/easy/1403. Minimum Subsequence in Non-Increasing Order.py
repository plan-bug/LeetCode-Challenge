class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        result = [nums.pop(nums.index(max(nums)))]
        print(result)
        while sum(result) <= sum(nums):
            result.append(nums.pop(nums.index(max(nums))))
        
        return result
            
