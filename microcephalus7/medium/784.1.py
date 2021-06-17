class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [""]
        for ch in s:
            res = [x + cc for x in res for cc in {ch, ch.swapcase()}]
        return res
