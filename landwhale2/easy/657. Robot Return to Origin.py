class Solution:
    def judgeCircle(self, moves: str) -> bool:
        up_down = 0
        left_right = 0
        for m in moves:
            if m == 'U':
                up_down += 1
            elif m == 'D':
                up_down -= 1
            elif m == 'L':
                left_right += 1
            elif m == 'R':
                left_right -= 1
        return not (up_down or left_right)
