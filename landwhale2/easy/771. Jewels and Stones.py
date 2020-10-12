class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        answer = 0
        for j in J:
            answer += S.count(j)
        return answer
