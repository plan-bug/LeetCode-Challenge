class Solution:
    def numberOfMatches(self, n: int) -> int:
        answer = 0
        while n != 1:
            result = n // 2
            n -= result
            answer += result
        
        return answer
