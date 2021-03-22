from typing import DefaultDict


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        freq = DefaultDict(int)
        for i in range(lowLimit, highLimit+1):
            freq[sum(int(j) for j in str(i) )]+=1
        return max(freq.values())