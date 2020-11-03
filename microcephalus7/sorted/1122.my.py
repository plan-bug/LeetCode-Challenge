# arr2 값 기준으로 정렬
# arr2 의 index 기준으로 정렬
# arr1 의 x 가 arr2 안에 존재 유/무 에 따른 정렬
# arr2 안에 존재하지 않을 시 arr2 길이에서 x 만큼 더한 index return


from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        return sorted(arr1, key=lambda x: arr2.index(x) if x in arr2 else len(arr2)+x)


solution = Solution()
print(solution.relativeSortArray(
    [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))
