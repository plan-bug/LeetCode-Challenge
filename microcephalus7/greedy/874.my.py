# for 문
# command 에서 i 값이 -1, -2 이냐에 따라 다음 좌표값 바뀜(우선 처리 필요)
# obstacles 값에 따른 처리 필요 (더하고 난 뒤 처리.)
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: [List[List[int]]]) -> int:
        x, y = 0, 0
        direction = 0
        formerCommand = 0
        for i in commands:
            if i == -1:
                if direction == 'N':
                    direction += 1
                elif direction == 'S':
                    direction = 'W'
                elif direction == 'E':
                    direction = 'S'
                else:
                    direction = 'N'
            elif i == -2:
                if direction == 'N':
                    direction = 'W'
                if direction == 'S':
                    direction = 'E'
                if direction == 'E':
                    direction = 'N'
                else:
                    direction = 'S'
            else:
                for j in range(i):
                    x += i
        return (x**2)+(y**2)


solution = Solution()
print(solution.robotSim([4, -1, 3], []))
