# enumrate 이용

class Solution:
    def runningSum(self,nums:List[int]) -> List[int]:
        newList = []
        for idx, val in enumerate(nums):
            newList.append(sum(nums[0:idx+1]))
        return newList