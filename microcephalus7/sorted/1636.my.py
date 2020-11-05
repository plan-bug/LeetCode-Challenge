# 먼저 거꾸로 뒤집음
# count 함수 이용하여 lambda 식으로 정렬
# 거꾸로 된건 역정렬

from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(sorted(nums, reverse=True), key=lambda x: nums.count(x))


solution = Solution()
print(solution.frequencySort([1, 1, 2, 2, 2, 3]))
print(solution.frequencySort([2, 3, 1, 3, 2]))
