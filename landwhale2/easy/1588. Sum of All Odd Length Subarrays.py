class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        start = 1
        add = 2
        result = 0
        for i in range(start, len(arr), add):
            for j in range(0, len(arr) + 1 - i):
                sum_ = 0
                for k in range(j, j+i):
                    sum_ += arr[k]
                result += sum_

        if len(arr) % 2 != 0:
            result += sum(arr)
        
        return result
 
 
 
