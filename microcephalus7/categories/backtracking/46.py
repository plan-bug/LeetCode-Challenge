# 순열
# 순서가 있는 조합
from itertools import permutations


class Solution:
    def permute(self, nums):
        return list(map(lambda x: list(x), permutations(nums)))


solution = Solution()
print(solution.permute(["A", "B", "C"]))
