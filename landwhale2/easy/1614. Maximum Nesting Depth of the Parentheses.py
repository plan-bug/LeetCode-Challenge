class Solution:
    def maxDepth(self, s: str) -> int:
        d=0
        m=0
        for i in s:
            if i=="(":
                d+=1
                if d>m:
                    m=d
            elif i==")":
                d-=1
        return m
