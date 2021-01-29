# slicing 이용
# s 기준으로 t 안에서 찾음
# 없을 시 return False
# 있을 시 해당 인덱스 다음에서 커팅

# s가 e의 순서대로 삭제한 list 라면
# s[i]에서 t를 커팅해도 s[i+1] 이 자른 t 안에 있음

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for char in s:
            idx = t.find(char)
            if idx == -1:
                return False
            t = t[idx+1:]
        return True


solution = Solution()
print(solution.isSubsequence('abc', 'ahbgdc'))
print(solution.isSubsequence('axc', 'ahbgdc'))
print(solution.isSubsequence('ace', 'abcde'))
print(solution.isSubsequence('aec', 'abcde'))
