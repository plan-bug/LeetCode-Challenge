# 전략
# expression 으로 배열 각 요소 추출된 list 세팅
# for 문 통해 A 요소 길이 만큼 indicing 된 list 생성
# if 문으로 정렬된 list 와 정렬 안 된 list 다를 시 count +1 씩함
# count return

from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        indicing = [list(i) for i in A]
        count = 0
        for j in range(len(A[0])):
            indice = [i[j] for i in indicing]
            if indice != sorted(indice):
                count += 1
        return count


solution = Solution()
print(solution.minDelectionSize(["zyx", "wvu", "tsr"]))
print(solution.minDelectionSize(["cba", "daf", "ghi"]))
