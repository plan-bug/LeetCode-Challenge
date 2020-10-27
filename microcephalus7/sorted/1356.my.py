# list 2진수로 변환
# 2진수 길이에 따른 정렬

from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        number = arr[0]
        binary = ""
        while number != 0:
            binary += str(number % 2)
            number = number // 2
        return number


solution = Solution()
print(solution.sortByBits([5]))
