class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        return reduce(lambda a, b: (a + b).removesuffix(part), s, "")


solution = Solution()
print(solution.removeOccurrences("aabababa", "aba"))
