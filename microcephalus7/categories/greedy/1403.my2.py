# 정렬 시킨 후 index 0 부터 대입

from typing import List


class Solution:
    def minSubsequence(self, nums: (List[int])) -> List[int]:
        sortedNums = sorted(nums, reverse=True)
        i = 0
        maximum = []
        while sum(maximum) <= sum(nums):
            maximum.append(sortedNums[i])
            nums.remove(sortedNums[i])
            i += 1
        return maximum


solution = Solution()
print(solution.minSubsequence([4, 4, 7, 6, 7]))
