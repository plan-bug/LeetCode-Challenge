
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output=[]
        def check(arr):
            if len(arr)<3:
                return True
            else:
                diff=arr[1]-arr[0]
            for i in range(len(arr)-1):
                if arr[i+1]-arr[i]==diff:
                    continue
                return False
            return True
        for i in range(len(l)):
            output.append(check(sorted(nums[l[i]:r[i]+1])))
        return output