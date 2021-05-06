class Solution:
    def countVowelStrings(self, n: int) -> int:
        sol = []
        arr = 'aeiou'
        def backtrack(arr,count,ans):
            if count == n:
                return sol.append(ans)
            for i in range(len(arr)):
                backtrack(arr[i:], count+1, ans+arr[i])
        backtrack(arr,0,'')
        return len(sol)