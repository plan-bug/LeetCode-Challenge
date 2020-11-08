# i,j 짝 맞춤
# comprehension 에 조건으로 해결

from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return len([(i, j)for i in range(len(nums)) for j in range(len(nums)) if i < j if nums[i] == nums[j]])


solution = Solution()
print(solution.numIdenticalPairs([1, 2, 3]))
print(solution.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
