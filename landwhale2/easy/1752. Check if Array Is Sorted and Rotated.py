from collections import deque

class Solution:
    def check(self, nums: List[int]) -> bool:
        d = deque(nums)
        sort = sorted(nums)
        for i in range(len(nums)):
            d.rotate(1)
            if list(d) == sort:
                return True
            
        return False
