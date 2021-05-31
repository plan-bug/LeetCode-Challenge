# s 돌며 () 각 몇개인지 파악
# (,) 차이 절대값 return

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        return abs(s.count("(")- s.count(")"))