from typing import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds = sum([j % 2 for i, j in Counter(s).items()])
        return len(s) if odds <= 1 else len(s) - odds + 1
