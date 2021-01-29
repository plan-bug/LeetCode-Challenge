# expression 이용
# 활/짝 리스트 생성
# min 함수로 짧은 쪽 길이 return

class Solution:
    def minCostToMoveChips(self, positions: List[int]) -> int:
        odd = [i for i in positions if i % 2 != 0]
        even = [i for i in positions if i % 2 == 0]
        return min(len(odd), len(even))
