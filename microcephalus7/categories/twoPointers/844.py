class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S = list(S)
        T = list(T)
        while "#" in S:
            if S.index("#") > 0:
                del S[S.index("#")-1]
            del S[S.index("#")]
        while "#" in T:
            if T.index("#") > 0:
                del T[T.index("#")-1]
            del T[T.index("#")]
        return ''.join(S) == ''.join(T)


solution = Solution()

print(solution.backspaceCompare("ab#c", "ad#c"))
print(solution.backspaceCompare("a##c", "#a#c"))
