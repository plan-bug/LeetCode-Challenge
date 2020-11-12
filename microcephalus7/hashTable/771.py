class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(map(lambda j: S.count(j), chain(J)))
