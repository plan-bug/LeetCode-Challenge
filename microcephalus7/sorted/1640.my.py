# pieces 조합 생성
# arr 와 일치하는 것이 있는 경우 true, 없을 경우 false


from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mp = {x[0]: x for x in pieces}
        res = []

        for num in arr:
            res += mp.get(num, [])
        return res == arr


solution = Solution()
print(solution.canFormArray([15, 88], [[88], [15]]))
