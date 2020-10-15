# while 문
# list 길이에 따라 breake
# list 안에서 최대값 2개 추출 (추출된 값 버림)
# 최대값 각각 뺀 수 list 안에 삽입 (뺀 수 0일 시 삽입 안 함)


from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while True:
            if(len(stones) == 1 or len(stones) == 0):
                break
            y = max(stones)
            stones.remove(y)
            x = max(stones)
            stones.remove(x)
            if y != x:
                stones.append(y-x)
        if stones == []:
            return 0
        else:
            return stones[0]


solution = Solution()
print(solution.lastStoneWeight([2, 7, 4, 1, 8, 1]))
