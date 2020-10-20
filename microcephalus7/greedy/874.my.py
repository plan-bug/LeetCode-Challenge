# for 문
# command 에서 i 값이 -1, -2 이냐에 따라 다음 좌표값 바뀜(우선 처리 필요)
# obstacles 값에 따른 처리 필요 (더하고 난 뒤 처리.)
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: [List[List[int]]]) -> int:
        x, y = 0, 0
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        number = 0
        for i in commands:
            if i == -1:
                number = (number+1) % 4
            elif i == -2:
                number -= 1
            else:
                number = (number-1) % 4
                for j in range(i):
                    if [x+direction[number][0], y+direction[number][1]] not in obstacles:
                        x += direction[number][0]
                        y += direction[number][1]
        return (x**2)+(y**2)


solution = Solution()
print(solution.robotSim([4, -1, 3], []))
print(solution.robotSim([4, -1, 4, -2, 4], [[2, 4]]))
