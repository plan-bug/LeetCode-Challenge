class Solution:
    def fib(self, N: int) -> int:
        if N == 0 or N == 1:
            return N
        
        dp = [0,1]
        
        for i in range(2, N+1):
            dp.append(dp[i-1] + dp[i-2])
        
        return dp[i]
