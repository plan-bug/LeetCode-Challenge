# for 문
# nums 돌며 0 있을 시 삭제
# append 로 0 삽입

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(0)


solution = Solution()
print(solution.moveZeroes([0, 1, 2, 3]))
