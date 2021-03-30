class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ids = [i for i in range(len(s)) if s[i] == c]
        return [min([abs(i-id_) for id_ in ids]) for i in range(len(s))]