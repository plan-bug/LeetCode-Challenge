class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = 0
        for i in range(n):
            nums ^= start+(2*i)
        return nums
        
