# 2중 컴프레션

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [len([j for j in nums if j < i])for i in nums]


solution = Solution()
print(solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
