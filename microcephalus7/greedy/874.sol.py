# 방위를 list 화.


class Solution(object):
    def robotSim(self, commands, obstacles):
        position_offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        obstacles = set(map(tuple, obstacles))
        x, y, direction, max_distance = 0, 0, 0, 0
        for command in commands:
            if command == -2:
                direction = (direction - 1) % 4
            elif command == -1:
                direction = (direction + 1) % 4
            else:
                x_off, y_off = position_offset[direction]
                while command:
                    if (x + x_off, y + y_off) not in obstacles:
                        x += x_off
                        y += y_off
                    command -= 1
                max_distance = max(max_distance, x**2 + y**2)
        print(x, y)
        return max_distance
        return obstacles
