class Solution:
    def generateTheString(self, n: int) -> str:
        return n%2 != 0 and 'a'*n or 'a'*(n-1) + 'b'