# for 문
# command 에서 i 값이 -1, -2 이냐에 따라 다음 좌표값 바뀜(우선 처리 필요)
# obstacles 값에 따른 처리 필요 (더하고 난 뒤 처리.)
# 튜플로 처리 필요
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: [List[List[int]]]) -> int:
        x, y, number, maxDistance = 0, 0, 0, 0
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for command in commands:
            if command == -1:
                number = (number+1) % 4
            elif command == -2:
                number = (number-1) % 4
            else:
                xOff, yOff = direction[number]
                while command:
                    if [x + xOff, y + yOff] not in obstacles:
                        x += xOff
                        y += yOff
                    command -= 1
                maxDistance = max(maxDistance, x**2 + y**2)
        print(x, y)
        return maxDistance


solution = Solution()
print(solution.robotSim([4, -1, 3], []))
print(solution.robotSim([4, -1, 4, -2, 4], [[2, 4]]))
