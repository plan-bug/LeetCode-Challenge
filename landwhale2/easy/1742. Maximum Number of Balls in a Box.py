class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = {}
        for i in range(lowLimit, highLimit + 1):
            num, s = i, 0 
            while num > 0:
                num, a = divmod(num, 10)
                s += a
            if s in d: 
                d[s] += 1
            else:
                d[s] = 1
        return max(d.values())
