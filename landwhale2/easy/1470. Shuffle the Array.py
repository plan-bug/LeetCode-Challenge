class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for x,y in zip(nums[:len(nums)//2], nums[len(nums)//2:]):
            result.append(x)
            result.append(y)
        return result
