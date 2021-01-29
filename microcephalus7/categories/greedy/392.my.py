# index 와 sorted index 차이 비교
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return [i for i in s if i in t]


solution = Solution()
print(solution.isSubsequence('abcde', 'ace'))
print(solution.isSubsequence('abcde', 'aec'))
