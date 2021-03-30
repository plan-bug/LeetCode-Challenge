class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        return [min([abs(i-id_) for id_ in [q for q in range(len(s)) if s[q] == c]]) for i in range(len(s))]