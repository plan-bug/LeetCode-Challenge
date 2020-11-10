# 딕셔너리 생성
# numbers 엘리먼트를 (인덱스, 요소값) 으로 나눔
# 키를 target 값을 요소값으로 뺀 수, 값을 해당값 index에 1 더한 수 의 쌍 딕셔너리에 넣음
# 다음 이터레이션에서 요소값이 딕셔너리에 있을 때 해당 요소 값과 지금 이터레이터 인덱스 return


from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i, e in enumerate(numbers):
            if e in dict:
                return (dict[e], i+1)
            dict[(target - e)] = i+1


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([2, 3, 4], 6))
print(solution.twoSum([5, 25, 75], 10))
