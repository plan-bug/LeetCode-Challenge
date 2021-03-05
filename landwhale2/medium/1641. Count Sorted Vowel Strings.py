class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0] * 6 for _ in range(n+1)]
        
        for i in range(1, 6):
            dp[1][i] = i
        
        for i in range(2, n+1):
            for j in range(1, 6):
                for k in range(1, j+1):
                    dp[i][j] += dp[i-1][k]

        return dp[n][5]
