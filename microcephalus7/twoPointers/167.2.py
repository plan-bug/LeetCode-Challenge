from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr = []
        for i, e in enumerate(numbers):
            if e in arr:
                return [arr.index(e)+1, i+1]
            arr.append(target-e)
