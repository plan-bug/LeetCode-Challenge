# 투 포인터 같은 개념
# 1을 기준으로 각 이터러블
# 1이 이터러블 보다 작으면 push, pop
# 같아졌을 때 push

# 반복해야할 땐 for, while

from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        currentNum = 1
        for num in target:
            while currentNum < num:
                operations.append("Push")
                operations.append("Pop")
                currentNum += 1
            operations.append("Push")
            currentNum += 1

        return operations


solution = Solution()
print(solution.buildArray([1, 3], 3))
