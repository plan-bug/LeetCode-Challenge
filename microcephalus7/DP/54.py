# 이터레이션
# 0 부터 시작하여 num[n] 에서 nums[i] 까지 합이 nums[n+1] 에서 nums[i]보다 클 경우 list에서 처음 수 유지/제거

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
