# enumrate 이용
# List 의 index 를 잘 이용하느냐
class Solution:
    def runningSum(self,nums:List[int]) -> List[int]:
        newList = []
        for i in range(len(nums)):
            newList.append(sum(nums[0:i+1]))
        return newList