class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums, reverse=True)
        target = nums_sorted[:2]
        arr = []
        for i in range(len(nums)):
            if nums[i] in target:
                arr.append(i)
                target.remove(nums[i])
            
            if len(arr) == 2:
                break
        
        return (nums[arr[0]]-1) * (nums[arr[1]]-1)
