# 간단한 stack
# ops 이터러블

from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        points = []
        for i in ops:
            if i == "+":
                points.append(sum(points[-2:]))
            elif i == 'D':
                points.append(2*points[-1])
            elif i == "C":
                points.pop()
            else:
                points.append(int(i))
        return sum(points)


solution = Solution()
print(solution.calPoints([]))
