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
