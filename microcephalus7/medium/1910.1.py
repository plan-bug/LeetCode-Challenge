class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        r = ""
        for i in s:
            r = (r + i).removesuffix(part)
        return r
