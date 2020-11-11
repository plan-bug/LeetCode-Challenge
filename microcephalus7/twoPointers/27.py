# nums 안에서 val가 없을떄까지
# del로 삭제

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            del nums[nums.index(val)]
        return nums


solution = Solution()
print(solution.removeElement([3, 2, 2, 3], 3))
print(solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
