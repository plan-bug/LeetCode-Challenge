# nums 에서 빼온 List 는 요소의 수가 가장 적지만 nums 나머지의 합보다 월등히 커야 한다.

# 계획
# List 에서 제일 큰 수와 나머지로 나눔
# 큰 수의 합이 나머지의 합 보다 커질때까지 반복.


from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        maximum = []
        while sum(maximum) <= sum(nums):
            maximum.append(max(nums))
            nums.remove(max(nums))
        return maximum


solution = Solution()
print(solution.minSubsequence([4, 4, 7, 6, 7]))
