

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = {}
        for i in range(lowLimit, highLimit+1):
            s=0
            while i>0:
                s+=i%10
                i = i//10
            if s not in d:
                d[s]=1
            else:
                d[s] +=1
        return max(d.values())