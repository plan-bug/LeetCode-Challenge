import itertools

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        combinations = itertools.combinations(range(3),n)