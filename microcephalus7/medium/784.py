# 가지 치기?
# string 돌며 요소가 영어일 때마다 가지 쳐짐
# 소문자? 소문자, 대문자
#


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [""]
        for ch in s:
            if ch.isalpha():
                res = [i + j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i + ch for i in res]
        return res
