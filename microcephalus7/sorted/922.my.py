# 짝/홀 로 list 분리
# 홀,짝,홀,짝 순으로 list 합체

from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = [i for i in A if i % 2 != 0]
        even = [i for i in A if i % 2 == 0]
        plus = []
        for i in range(len(odd)):
            plus.append(even[i])
            plus.append(odd[i])
        return plus


solution = Solution()
print(solution.sortArrayByParityII([4, 2, 5, 7]))
