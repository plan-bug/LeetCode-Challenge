# 조합 구하기
# 첫 요소부터 끝 요소까지 누적해서 반복 연산 하는 함수 찾아서 대입 후 return


from itertools import combinations
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        bits = 0
        for i in nums:
            bits |= i
        return bits * int(pow(2, len(nums) - 1))


solution = Solution()
print(solution.subsetXORSum([1, 3]))
