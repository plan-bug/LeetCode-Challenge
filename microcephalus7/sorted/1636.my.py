from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(sorted(nums, reverse=True), key=lambda x: nums.count(x))


solution = Solution()
print(solution.frequencySort([1, 1, 2, 2, 2, 3]))
print(solution.frequencySort([2, 3, 1, 3, 2]))
