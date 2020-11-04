# pieces 요소의 첫 번째 값을 키, 요소를 value 로 하는 객체 만듦
# arr 돌며 arr의 요소가 객체의 key 로 있는지 확인하고 있을 시 res 값에 넣음
# 다 만들어진 res 가 arr 값과 일치하는지 값 return


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
print(solution.canFormArray([49, 18, 16], [[16, 18, 49], [13, 23, 24]]))
