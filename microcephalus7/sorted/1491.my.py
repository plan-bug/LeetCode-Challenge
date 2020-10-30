# list 에서 함수로 max, min 삭제 (or 정렬 후 첫번째, 마지막 삭제)
# 평균 값 return

from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        return sum(sorted(salary)[1:len(salary)-1])/len(sorted(salary)[1:len(salary)-1])
