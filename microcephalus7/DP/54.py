# 이터레이션
# max 로 최댓값 유지
# 121번과 함께 공부 필요

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        newNum = maxTotal = nums[0]

        for i in range(1, len(nums)):
            newNum = max(nums[i], nums[i]+newNum)
            maxTotal = max(newNum, maxTotal)
        return maxTotal


solution = Solution()
print(solution.maxSubArray(
    [-2, 1, -3, 4, -1, 2, 1, -5, 4]))
