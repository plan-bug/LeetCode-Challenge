# 2칸씩 이동하면 cost = 0, 1칸씩 이동 시 cost = 1 에서 홀/짝의 논리가 존재한다는 것을 파악


# 짝수, 홀수 중 제일 적은 쪽이 덜 이동시킨다.
# for 문으로 짝, 홀수 판별 후 counting
# min 함수로 적은 쪽 return

class Solution:
    def minCostToMoveChips(self, positions: List[int]) -> int:
        odd = 0
        even = 0
        for i in positions:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(even, odd)
