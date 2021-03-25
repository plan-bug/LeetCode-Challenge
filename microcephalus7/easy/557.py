class Solution:
    def reverseWords(self, s: str) -> str:
        return' '.join([''.join(reversed(list(i))) for i in s.split(" ")])