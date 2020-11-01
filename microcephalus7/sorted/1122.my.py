# arr2 값 기준으로 정렬
#


from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()
        return arr1
