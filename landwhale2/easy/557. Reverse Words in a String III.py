class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([n[::-1] for n in s.split()])
