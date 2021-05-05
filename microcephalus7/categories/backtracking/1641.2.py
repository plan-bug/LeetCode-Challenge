class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [0] + [1]*5
        for i in range(n):
            dp = accumulate(dp)
        return list(dp)[-1]